from yattag import Doc, indent
import csv
import os,sys


class MEBT():
    def __init__(self):
        import yaml
        self.dict=yaml.load(open(os.path.join(os.path.dirname(sys.argv[0]),'dictionary.yml'),'r').read())['MEBT']

        self.doc, self.tag, self.text = Doc().tagtext()

    def append(self,element, essname, insightLink, model, section, aperture, index, slot_number, slot_type, doorsid, elementEnergy, TCSz, TCSy, MCSz, MCSy):

        # Add the RFQ block:
        if element == 'BCM' and section == 'RFQ':
            if section == 'RFQ':
                with self.tag('div', klass="element BLE", index=index, essname=essname, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id="RFQ"):
                   self.doc.stag('img', klass="element_img", src=self.dict['RFQ']['src'])

        if element in ['Grid', 'QV', 'QH', 'BPM', 'Chop', 'ChDump', 'WS', 'Cav', 'Coll', 'BLM', 'NPM', 'EMU', 'LBM', 'FC', 'BCM']:
            if model:
                base=self.dict[element][model]
            else:
                base=self.dict[element]
            if slot_type and slot_type in base:
                base=base[slot_type]

            with self.tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
              self.doc.stag('img', klass="element_img", src=base['src'])

        elif element not in ['Drf', 'RFC']:
            # Print ignored elements (to check we are taking all)
            print("Ignoring element",element,"in MEBT")

    def write(self):

        combined_html = indent(self.doc.getvalue())

        text_file = open(os.path.join('C:\\newGit\\BD Viewer','templates','Synoptic.html'), "a")
        text_file.write(combined_html)
        text_file.close()
