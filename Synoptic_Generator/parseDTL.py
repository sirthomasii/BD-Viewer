from yattag import Doc, indent
import csv
import os,sys

class DTL():
    def __init__(self):
        import yaml
        self.dict=yaml.load(open(os.path.join(os.path.dirname(sys.argv[0]),'dictionary.yml'),'r').read())['DTL']

        self.doc, self.tag, self.text = Doc().tagtext()
        self.inDTL = False
        self.current_DTL = 1

    def append(self, element, essname, insightLink, model, section, aperture, index, slot_number, slot_type, doorsid, elementEnergy, TCSz, TCSy, MCSz, MCSy):


        # First deal with DT starts..
        if element == 'QV' and index == 1 and not self.inDTL:
            self.inDTL = True
            with self.tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id="DTC Start"):
               #text('index = '+index)
               self.doc.stag('img', klass="element_img", src=self.dict['DTC_Start']['src'])

        if element in ('QV', 'QH', 'BLM', 'CV', 'CH', 'BPM', 'NPM', 'FC', 'BCM', 'LBM', 'BLM'):
            if model:
                base=self.dict[element][model]
            else:
                base=self.dict[element]
            if slot_type and slot_type in base:
                base=base[slot_type]

            # If PMQ we want to show this as the element type
            if 'PMQ' in doorsid:
                _id=doorsid
            else:
                _id=element

            with self.tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=_id):
               #text('index = '+index)
               self.doc.stag('img', klass="element_img", src=base['src'])

        elif (element == 'DTC'):
            if index == 1 and self.current_DTL>1:
                self.inDTL = True
                with self.tag('div', klass="element BLE", index=index, essname=essname, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id="DTC Start"):
                   #text('index = '+index)
                   self.doc.stag('img', klass="element_img", src=self.dict['DTC_Start']['src'])
            elif index == self.dict['DTC_End']['ncells'][self.current_DTL]:
                self.inDTL = False
                self.current_DTL += 1
                with self.tag('div', klass="element BLE", index=index, essname=essname, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id="DTC End"):
                   #text('index = '+index)
                   self.doc.stag('img', klass="element_img", src=self.dict['DTC_End']['src'])

        elif element not in ['Drf']:
            # Print ignored elements (to check we are taking all)
            print("Ignoring element",element,"in DTL")

    def write(self):
        combined_html = indent(self.doc.getvalue())

        text_file = open(os.path.join('C:\\newGit\\BD Viewer','templates','Synoptic.html'), "a")
        text_file.write(combined_html)
        text_file.close()
