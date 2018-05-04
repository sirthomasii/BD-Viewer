from yattag import Doc, indent
import csv
import os,sys

class A2T():
    def __init__(self):
        import yaml
        self.dict=yaml.load(open(os.path.join(os.path.dirname(sys.argv[0]),'dictionary.yml'),'r').read())['A2T']

        self.doc, self.tag, self.text = Doc().tagtext()


    def append(self, element, essname, insightLink, model, section, aperture, index, slot_number, slot_type, doorsid, elementEnergy, TCSz, TCSy, MCSz, MCSy):

        if element in ('QV', 'QH', 'BPM', 'Grd', 'CX', 'Img', 'Cav', 'WS', 'NPM', 'FC', 'BCM', 'LBM', 'BLM', 'Col', 'AptM', 'EMU', 'DPL', 'DV', 'SLIT', 'RstH', 'RstV', 'Valve', 'Pump'):

            if model:
                base=self.dict[element][model]
            else:
                base=self.dict[element]
            if slot_type and slot_type in base:
                base=base[slot_type]


            with self.tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
               #text('index = '+index)
               self.doc.stag('img', klass="element_img", src=base['src'])

            # Special treatment of Target (does not exist in CSV)
            if element == 'Img' and slot_type == "PBDPlg" and index == 1:
               with self.tag('div', klass="element BLE", index=1, essname='TARGET', model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=(TCSz+self.dict['TGT']['zShift']), tcs_y=TCSy, mcs_y=MCSy, mcs_z=(MCSz+self.dict['TGT']['zShift']), id="TGT"):
                  #text('index = '+index)
                  self.doc.stag('img', klass="element_img", src=self.dict['TGT']['src'])

        # elif element == 'Drf':
        #     base=self.dict['Drf']
        #     if slot_number in base and slot_type in base[slot_number] and index in base[slot_number][slot_type]:
        #         drf_type=base[slot_number][slot_type][index]
        #         with self.tag('div', klass="element BLE", index=index, essname="n/a", insightLink="n/a", model="n/a", slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=self.dict['Valve'][drf_type]['id']):
        #           #text('index = '+index)
        #            self.doc.stag('img', klass="element_img", src=self.dict['Valve'][drf_type]['src'])

        elif element not in ['Drf']:
            # Print ignored elements (to check we are taking all)
            print("Ignoring element",element,"in A2T")


    def write(self):

        combined_html = indent(self.doc.getvalue())

        text_file = open(os.path.join('C:\\newGit\\BD Viewer','templates','Synoptic.html'), "a")
        text_file.write(combined_html)
        text_file.close()
