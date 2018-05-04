from yattag import Doc
import csv
import os,sys

doc, tag, text = Doc().tagtext()


def parseRFQ(element, essname, insightLink, model, section, aperture, index, slot_number, slot_type, elementEnergy, TCSz, TCSy, MCSz, MCSy):
    #print(element)
    #print(index)

    if element == 'RFC':
       with tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
          doc.stag('img', klass="element_img", src='https://i.imgur.com/dW6zgqU.jpg')
    elif element == 'ChDump':
       with tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
          doc.stag('img', klass="element_img", src='https://i.imgur.com/XNm5HUR.jpg')
    elif element == 'Chop':
        with tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
           doc.stag('img', klass="element_img", src='https://i.imgur.com/OsTAHm8.jpg')
    if element == 'QV':
        with tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
           #text('index = '+index)
           doc.stag('img', klass="element_img", src='https://i.imgur.com/1JXeiYU.jpg')
    elif element == 'QH':
        with tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
           #text('index = '+index)
           doc.stag('img', klass="element_img", src='https://i.imgur.com/rse8MN6.jpg')
    elif element == 'BPM':
        with tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
           #text('index = '+index)
           doc.stag('img', klass="element_img", src='https://i.imgur.com/BlqNMhD.jpg')
    elif element == 'Cav':
        with tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
           #text('index = '+index)
           doc.stag('img', klass="element_img", src='https://i.imgur.com/dpwwhsH.jpg')
    elif element == 'WS':
        with tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
           doc.stag('img', klass="element_img", src='https://i.imgur.com/X7FpG5X.jpg')
    elif element == 'NPM':
        if model == 'IPM':
            with tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
               doc.stag('img', klass="element_img", src='https://i.imgur.com/L90HaqZ.jpg')
        if model == 'BIF':
            with tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
               doc.stag('img', klass="element_img", src='https://i.imgur.com/mOCLAws.jpg')

    elif (element == 'FC'):
        with tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
           doc.stag('img', klass="element_img", src='https://i.imgur.com/6iJS7Ku.jpg')
    elif element == 'FBCM':
        with tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
           doc.stag('img', klass="element_img", src='https://i.imgur.com/vMMTDR9.jpg')
    elif element == 'BCM':
        with tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
           doc.stag('img', klass="element_img", src='https://i.imgur.com/yYu1pPC.jpg')
    elif element == 'LBM':
        with tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
           doc.stag('img', klass="element_img", src='https://i.imgur.com/uKcAuL0.jpg')
    elif element == 'BLM':
        if model == 'nBLM':
            with tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
               doc.stag('img', klass="element_img", src='https://i.imgur.com/yPK1UU8.jpg')
        if model == 'ICBLM':
            with tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
               doc.stag('img', klass="element_img", src='https://i.imgur.com/eykYmvU.jpg')

    elif element == 'Col':
        with tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
           doc.stag('img', klass="element_img", src='https://i.imgur.com/9jZuBfA.jpg')
    elif element == 'APTM':
       with tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
          doc.stag('img', klass="element_img", src='https://i.imgur.com/nb6TgRG.jpg')
    elif element == 'EMU':
       with tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
          doc.stag('img', klass="element_img", src='https://i.imgur.com/conggKa.jpg')
    elif element == 'DPL':
       with tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
          doc.stag('img', klass="element_img", src='https://i.imgur.com/XNm5HUR.jpg')
    elif element == 'BND':
       with tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
          doc.stag('img', klass="element_img", src='https://i.imgur.com/XtaJvjG.jpg')
    elif element == 'Slit':
       with tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
          doc.stag('img', klass="element_img", src='https://i.imgur.com/kGqn6S9.jpg')
    elif element == 'CX':
        with tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
           #text('index = '+index)
           doc.stag('img', klass="element_img", src='https://i.imgur.com/AJVSECY.jpg')

    #print(doc.getvalue())
    #print(index)

    combined_html = doc.getvalue()
    #print(doc.getvalue())
    text_file = open(os.path.join('C:\\newGit\\BD Viewer','templates','Synoptic.html'), "a")
    text_file.write(combined_html)
    text_file.close()

    return
