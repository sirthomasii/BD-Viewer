from yattag import Doc, indent
import csv
import os,sys

class LEBT():
    def __init__(self):
        import yaml
        self.dict=yaml.load(open(os.path.join(os.path.dirname(sys.argv[0]),'dictionary.yml'),'r').read())['LEBT']

        self.doc, self.tag, self.text = Doc().tagtext()

    def append(self, element, essname, insightLink, model, section, aperture, index, slot_number, slot_type, elementEnergy, TCSz, TCSy, MCSz, MCSy):
        #print(type(index))

        # Add IS element
        if (element == 'Drf' and index == 1 and section == 'ISrc'):
            with self.tag('div', klass="element BLE", index=index, essname=essname, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=(TCSz-83.05), tcs_y=TCSy, mcs_y=MCSy, mcs_z=(MCSz-83.05), id="IS"):
               #text('index = '+index)
               self.doc.stag('img', klass="element_img", src=self.dict['IS']['src'])

        if element in ('FC', 'NPM', 'BCM', 'Sol', 'Coll', 'Iris', 'Chop', 'Dpl', 'EMU'):

            if model:
                base=self.dict[element][model]
            else:
                base=self.dict[element]
            if slot_type and slot_type in base:
                base=base[slot_type]

            with self.tag('div', klass="element BLE", index=index, essname=essname, insightLink=insightLink, model=model, slot_type=slot_type, slot_number=slot_number, aperture=aperture, elementEnergy=elementEnergy, section=section, tcs_z=TCSz, tcs_y=TCSy, mcs_y=MCSy, mcs_z=MCSz, id=element):
              self.doc.stag('img', klass="element_img", src=base['src'])

        elif element not in ['Drf']:
            # Print ignored elements (to check we are taking all)
            print("Ignoring element",element,"in LEBT")


    def write(self):
        fin = open('C:\\newGit\\BD Viewer\\Synoptic_Generator\\htmlHeader2.html', "r")
        headerData2 = fin.read()

        combined_html = headerData2 + indent(self.doc.getvalue())

        text_file = open(os.path.join('C:\\newGit\\BD Viewer','templates','Synoptic.html'), "a")
        text_file.write(combined_html)
        text_file.close()
