import os
from flask import Flask,render_template, request,json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

import time
import datetime
import subprocess
from threading import Thread
import threading
import os
import BPM
from BPM import BPMdata, triggerAquisition
import math
import numpy as np

try:
    import ujson as json
    print("ujson")
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        import json
from scipy.stats import gaussian_kde

npm_frame = 1
npm_filenum = 1
IMG_frame = 1
IMG_filenum = 1
IMG_x = 0
IMG_y = 0
IMG_firstRun = True

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/SynopticPV')
def SynoptpicPV():
    return render_template('SynopticPV.html')
@app.route('/Synoptic')
def Synoptpic():
    return render_template('Synoptic.html')


def writeBPMdata(bpm):
    # data = str(list(bpm.sumSigAmpSpectrum()))
    fs = 50 # sample rate
    f = 2 # the frequency of the signal
    millis = int(round(time.time() * 1000))
    x = np.arange(fs) # the points on the x axis for plotting
    # compute the value (amplitude) of the sin wave at first sample
    y_0 = np.sin(2*np.pi*f * (1/fs)-millis)
    while(y_0 < .9999):
        millis = int(round(time.time() * 1000))
        y_0 = np.sin(2*np.pi*f * (1/fs)-millis)
    AMP = 1*abs(np.sin(millis/100000))
    # compute the value (amplitude) of the sin wave at the for each sample
    y = [ AMP*np.sin(2*np.pi*f * (i/fs)-millis) for i in np.arange(fs)]
    data_x = x
    data_y = y
    with open('static/db/BPM_DATA.json', 'w') as outfile:
        bpm_data = {}
        bpm_data['bpm_x'] = []
        bpm_data['bpm_y'] = []
        for i in range(1,len(data_y)):
            bpm_data["bpm_x"].append(str(data_x[i]))
            bpm_data["bpm_y"].append(str(data_y[i]))
        json.dump(bpm_data, outfile)
    threading.Timer(.07, writeBPMdata, [bpm]).start()
    return "writing BPM data"

def writeIMGdata(IMG):
    global IMG_frame
    global IMG_filenum
    global IMG_x
    global IMG_y
    global IMG_firstRun
    IMG_filename = 'static/db/IMG/IMG_DATA_'+str(IMG_filenum)+'.json'
    millis = int(round(time.time() * 1000))
    if (IMG_firstRun == True):
        # Generate fake data
        IMG_x = np.random.normal(size=50)
        IMG_y = IMG_x*2 + np.random.normal(size=50)
        IMG_firstRun = False
        x = IMG_x
        y = IMG_y

    else:
        x = IMG_x*.5*(1+abs(np.cos(millis/50000)))
        y = IMG_y*.5*(1+abs(np.sin(millis/50000)))
    # Calculate the point density
    xy = np.vstack([x,y])
    z = gaussian_kde(xy)(xy)

    data_x = x
    data_y = y
    data_z = z

    if(IMG_frame > 1):
        data = json.load(open(IMG_filename))
        with open(IMG_filename, 'w') as outfile:
            IMG_data = {}
            IMG_data[IMG_frame] = {}
            IMG_data[IMG_frame]['x'] = []
            IMG_data[IMG_frame]['y'] = []
            IMG_data[IMG_frame]['z'] = []

            for i in range(1,len(data_x)):
                IMG_data[IMG_frame]["x"].append(str(data_x[i]))
                IMG_data[IMG_frame]["y"].append(str(data_y[i]))
            for j in range(1,len(data_z)):
                IMG_data[IMG_frame]["z"].append(str(data_z[j]*abs(np.sin(j*.5))))
            data[IMG_frame] = IMG_data[IMG_frame]
            json.dump(data, outfile)
    else:
        with open(IMG_filename, 'w') as outfile:
            IMG_data = {}
            IMG_data[IMG_frame] = {}
            IMG_data[IMG_frame]['x'] = []
            IMG_data[IMG_frame]['y'] = []
            IMG_data[IMG_frame]['z'] = []
            for i in range(1,len(data_x)):
                IMG_data[IMG_frame]["x"].append(str(data_x[i]))
                IMG_data[IMG_frame]["y"].append(str(data_y[i]))
            for j in range(1,len(data_z)):
                IMG_data[IMG_frame]["z"].append(str(data_z[j]))
            json.dump(IMG_data, outfile)

    if(IMG_frame < 28):
        IMG_frame += 1
    else:
        IMG_frame = 1
        if IMG_filenum < 10:
            IMG_filenum += 1
        else:
            IMG_filenum = 1
    threading.Timer(.03, writeIMGdata, [IMG]).start()
    return "writing Scatter data"

def writeNPMdata(npm):
    global npm_frame
    global npm_filenum
    npm_filename = 'static/db/NPM/NPM_DATA_'+str(npm_filenum)+'.json'
    # data = str(list(bpm.sumSigAmpSpectrum()))
    fs = 20 # sample rate
    f = .1 # the frequency of the signal
    fs_z = fs*fs # sample rate
    millis = int(round(time.time() * 1000))
    x = np.arange(fs) # the points on the x axis for plotting
    y = np.arange(fs) # the points on the x axis for plotting
    # compute the value (amplitude) of the sin wave at the for each sample
    z = [ np.sin((2*np.pi*f * (i/fs)) - millis/10000) for i in np.arange(fs_z)]
    data_x = x
    data_y = y
    data_z = z
    if(npm_frame > 1):
        data = json.load(open(npm_filename))
        with open(npm_filename, 'w') as outfile:
            npm_data = {}
            npm_data[npm_frame] = {}
            npm_data[npm_frame]['x'] = []
            npm_data[npm_frame]['y'] = []
            npm_data[npm_frame]['z'] = []

            for i in range(1,len(data_x)):
                npm_data[npm_frame]["x"].append(str(data_x[i]))
                npm_data[npm_frame]["y"].append(str(data_y[i]))
            for j in range(1,len(data_z)):
                npm_data[npm_frame]["z"].append(str(data_z[j]*abs(np.sin(j*.5))))
            data[npm_frame] = npm_data[npm_frame]
            json.dump(data, outfile)
    else:
        with open(npm_filename, 'w') as outfile:
            npm_data = {}
            npm_data[npm_frame] = {}
            npm_data[npm_frame]['x'] = []
            npm_data[npm_frame]['y'] = []
            npm_data[npm_frame]['z'] = []
            for i in range(1,len(data_x)):
                npm_data[npm_frame]["x"].append(str(data_x[i]))
                npm_data[npm_frame]["y"].append(str(data_y[i]))
            for j in range(1,len(data_z)):
                npm_data[npm_frame]["z"].append(str(data_z[j]*abs(np.sin(j*.5))))
            json.dump(npm_data, outfile)

    if(npm_frame < 28):
        npm_frame += 1
    else:
        npm_frame = 1
        if npm_filenum < 10:
            npm_filenum += 1
        else:
            npm_filenum = 1
    threading.Timer(.04, writeNPMdata, [npm]).start()
    return "writing NPM data"

@app.route('/getLastNPMfileNum', methods=['GET'])
def getLastNPMfileNum():
    if npm_filenum > 1:
        last_good_npm_filenum = npm_filenum -1
    else:
        last_good_npm_filenum = 1
    return str(last_good_npm_filenum)

@app.route('/getLastIMGfileNum', methods=['GET'])
def getLastIMGfileNum():
    if IMG_filenum > 1:
        last_good_IMG_filenum = IMG_filenum -1
    else:
        last_good_IMG_filenum = 1
    return str(last_good_IMG_filenum)

# triggerAquisition()
# bpm1 = BPMdata(1)
# bpm2 = BPMdata(2)
# writeBPMdata(bpm1)
# writeNPMdata(bpm2)
# writeIMGdata(bpm2)

if __name__=="__main__":

    app.run(host= '0.0.0.0')
