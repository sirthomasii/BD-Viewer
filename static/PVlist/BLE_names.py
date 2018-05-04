import csv
import sys,os
import json

#OPEN THE TARGET CSV AND SPIT THE COLUMNS INTO PYTHON LISTS
with open("E:\\newGit\\BD Viewer\\static\\PVlist\\BLEs.csv")  as csvfile:

     rows = csv.reader(csvfile)
     res = list(zip(*rows))

     content={}
     for r in res:
         BLEs=list(r)
BLE_names = []
for BLE_name in BLEs:
    BLE_name_new = BLE_name.split(":")
    BLE_name_new_0 = BLE_name_new[0].split("-")
    BLE_name_new_1 = BLE_name_new[1].split("-")
    BLE_name_new = []
    BLE_name_new.append(BLE_name_new_0[0])
    BLE_name_new.append(BLE_name_new_0[1])
    BLE_name_new.append(BLE_name_new_1[0])
    BLE_name_new.append(BLE_name_new_1[1])
    BLE_name_new.append(BLE_name_new_1[2])
    BLE_names.append(BLE_name_new)

BLE_data={}
#BULD SECTIONS
for BLE_name in BLE_names:
    BLE_data[BLE_name[0]] = {}
#BUILD CELLS
for BLE_name in BLE_names:
    BLE_data[BLE_name[0]][BLE_name[1]] = {}
#BUILD DISC
for BLE_name in BLE_names:
    BLE_data[BLE_name[0]][BLE_name[1]][BLE_name[2]] = {}
#BUILD ELEM
for BLE_name in BLE_names:
    BLE_data[BLE_name[0]][BLE_name[1]][BLE_name[2]][BLE_name[3]] = {}
#BUILD INDEX, PVTYPE
for BLE_name in BLE_names:
    BLE_data[BLE_name[0]][BLE_name[1]][BLE_name[2]][BLE_name[3]][BLE_name[4]] = ["X", "Y"]

BLE_data = str(BLE_data)
BLE_data = BLE_data.replace("\'","\"")
parsed = json.loads(BLE_data)
#BLE_data[BLE_name[0]] = {BLE_name[1]}
#print (json.dumps(parsed, indent=2, sort_keys=True))

#print(BLE_data)
with open("E:\\newGit\\BD Viewer\\static\\PVlist\\BLEs_detail.json",'w') as file:
    file.write(BLE_data)

BLE_names = []
for BLE_name in BLEs:
    BLE_name_new = BLE_name.split(":")
    BLE_name_new_0 = BLE_name_new[0].split("-")
    BLE_name_new_1 = BLE_name_new[1]

    BLE_name_new = []
    BLE_name_new.append(BLE_name_new_0[0])
    BLE_name_new.append(BLE_name_new_0[1])
    BLE_name_new.append(BLE_name_new_1)
    BLE_names.append(BLE_name_new)
#print(BLE_names)
BLE_data={}
#BULD SECTIONS
for BLE_name in BLE_names:
    BLE_data[BLE_name[0]] = {}
#BUILD CELLS
for BLE_name in BLE_names:
    BLE_data[BLE_name[0]][BLE_name[1]] = []
#BUILD DISC
for BLE_name in BLE_names:
    BLE_data[BLE_name[0]][BLE_name[1]].append(BLE_name[2])

BLE_data = str(BLE_data)
BLE_data = BLE_data.replace("\'","\"")
parsed = json.loads(BLE_data)
#BLE_data[BLE_name[0]] = {BLE_name[1]}
#print (json.dumps(parsed, indent=2, sort_keys=True))

#print(BLE_data)
with open("E:\\newGit\\BD Viewer\\static\\PVlist\\BLEs_readable.json",'w') as file:
    file.write(BLE_data)

##########################################################################################
#BUILD PV-BLE ASSOCIATION JSON

BLE_names = []
BLE_data={}

for BLE_name in BLEs:
    BLE_name_new = BLE_name.split(":")
    BLE_name_new_0 = BLE_name_new[0].split("-")
    BLE_name_new_1 = BLE_name_new[1]

    BLE_name_new = []
    BLE_name_new.append(BLE_name_new_0[0])
    BLE_name_new.append(BLE_name_new_0[1])
    BLE_name_new.append(BLE_name_new_1)
    BLE_names.append(BLE_name_new)
#print(BLE_names)
#BULD BLE LIST
for BLE_name in BLEs:
    BLE_data[BLE_name] = {}
    BLE_data[BLE_name]["suffixes"] = []
    BLE_data[BLE_name]["plotTypes"] = []
    if "NPM" in BLE_name:
        BLE_data[BLE_name]["suffixes"].append("Img")

    if "BPM" in BLE_name:
        BLE_data[BLE_name]["suffixes"].append("Xpos")
        BLE_data[BLE_name]["suffixes"].append("Ypos")
        BLE_data[BLE_name]["suffixes"].append("Phase")
        BLE_data[BLE_name]["suffixes"].append("Img")

        BLE_data[BLE_name]["plotTypes"].append("scatter")
        BLE_data[BLE_name]["plotTypes"].append("scatter + line")
        BLE_data[BLE_name]["plotTypes"].append("timeSeries")
        BLE_data[BLE_name]["plotTypes"].append("contour")
        BLE_data[BLE_name]["plotTypes"].append("heatMap")
        BLE_data[BLE_name]["plotTypes"].append("surface")

BLE_data = str(BLE_data)
BLE_data = BLE_data.replace("\'","\"")
parsed = json.loads(BLE_data)
#BLE_data[BLE_name[0]] = {BLE_name[1]}
print (json.dumps(parsed, indent=2, sort_keys=True))

#print(BLE_data)
with open("E:\\newGit\\BD Viewer\\static\\PVlist\\BLE-PV.json",'w') as file:
    file.write(BLE_data)
