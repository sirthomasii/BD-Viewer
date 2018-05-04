from yattag import Doc, indent
import csv
import os,sys



class SPK():
    def __init__(self):
        import yaml
        self.dict=yaml.load(open(os.path.join(os.path.dirname(sys.argv[0]),'dictionary.yml'),'r').read())['SPK']

        self.doc, self.tag, self.text = Doc().tagtext()

        self.current_CM_TCS_z_start = 0
        self.current_CM_MCS_z_start = 0

    def append(self, element, essname, insightLink, model, section, aperture, index, slot_number, slot_type, elementEnergy, TCSz, TCSy, MCSz, MCSy):

        if element in ('QV', 'QH', 'BPM', 'BLM', 'CX', 'LBM', 'IBS', 'NPM', 'WS'):
            if model:
                base=self.dict[element][model]
            else:
                base=self.dict[element]
            if slot_type and slot_type in base:
                base=base[slot_type]
            with self.tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
               #text('index = '+index)
               self.doc.stag('img', klass="element_img", src=base['src'])
        elif (element == 'Cav') and (index == 1):
            self.current_CM_TCS_z_start = TCSz
            self.current_CM_MCS_z_start = MCSz
            with self.tag('div', klass="element BLE", index=index, essname="n/a", insightLink="n/a", model="n/a", slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=self.dict['Valve']['DN63']['id']):
              #text('index = '+index)
               self.doc.stag('img', klass="element_img", src=self.dict['Valve']['DN63']['src'])

        elif (element == 'Cav') and (index == 2):
            current_CM_TCS_z_end = TCSz
            current_CM_MCS_z_end = MCSz
            current_CM_TCS_z_middle = (self.current_CM_TCS_z_start + current_CM_TCS_z_end)/2
            current_CM_MCS_z_middle = (self.current_CM_MCS_z_start + current_CM_MCS_z_end)/2
            with self.tag('div', klass="element BLE", index=index, essname=essname, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=current_CM_TCS_z_middle, tcs_y=TCSy, mcs_y=MCSy, mcs_z=current_CM_MCS_z_middle, id=element):
               #text('index = '+index)
               self.doc.stag('img', klass="element_img", src=self.dict[element]['src'])
            with self.tag('div', klass="element BLE", index=index, essname="n/a", insightLink="n/a", model="n/a", slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=self.dict['Valve']['DN63']['id']):
              #text('index = '+index)
               self.doc.stag('img', klass="element_img", src=self.dict['Valve']['DN63']['src'])

        elif element not in ['Drf']:
            # Print ignored elements (to check we are taking all)
            print("Ignoring element",element,"in SPK")


    def write(self):
        #print(doc.getvalue())
        #print(index)
        combined_html = indent(self.doc.getvalue())
        #print(doc.getvalue())
        text_file = open(os.path.join('C:\\newGit\\BD Viewer','templates','Synoptic.html'), "a")
        text_file.write(combined_html)
        text_file.close()
