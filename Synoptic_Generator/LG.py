from yattag import Doc
from distutils.dir_util import copy_tree
import parseLEBT, parseMEBT, parseSPK, parseMBL, parseHBL, parseHEBT, parseA2T, parseDTL, parseDumpL
import parsetools
import csv
import sys,os

#CLEAN THE HTML FILES
open('C:\\newGit\\BD Viewer\\templates\\Synoptic.html', 'w').close()
# Allow first argument to be path to csv file
if len(sys.argv)>1:
    ELEMENTS_CSV=sys.argv[1]
    ELEMENTS_CSV_DMPL=sys.argv[2]
else:
    folder='C:\\newGit\\BD Viewer\\Synoptic_Generator\\CSV_Tables'
    for i in range(3):
        if os.path.exists(folder):
            break
        folder=os.path.join(folder)
    ELEMENTS_CSV=os.path.join(folder, 'TARGET', 'elements.csv')
    ELEMENTS_CSV_DMPL=os.path.join(folder, 'DUMP', 'elements.csv')

#OPEN THE TARGET CSV AND SPIT THE COLUMNS INTO PYTHON LISTS
with open(ELEMENTS_CSV)  as csvfile:

     rows = csv.reader(csvfile, delimiter=',', quotechar='"')
     headers = next(rows)

     res = list(zip(*rows))

     # First and last line should be removed,
     # we make it a bit more generic (in case of future changes)
     removes=[]
     for i in range(len(res[0])):
         if res[0][i]=='':
             removes.append(i)
     removes.sort(reverse=True)
     content={}
     for h,r in zip(headers,res):
         r=list(r)
         for i in removes:
             del r[i]
         content[h]=r
section = content['sect']
slot_number = content['cell']
slot_type = content['slot']
element = content['elem']
index = content['index']
essname = content['essname']
aperture = content['r[mm]']
doorsid = content['doorsid']
TCSz = content['TCS,m,z[mm]']
TCSy = content['TCS,m,y[mm]']
MCSz = content['MCS,m,z[mm]']
MCSy = content['MCS,m,y[mm]']
model = content['model']

#CONVERT TO LISTS
section = list(section)
essname = list(essname)
model = list(model)
slot_type = list(slot_type)
element = list(element)
index = list(map(int, index))
slot_number = list(slot_number)
TCSz = list(map(float, TCSz))
TCSy = list(map(float, TCSy))
MCSz = list(map(float, MCSz))
MCSy = list(map(float, MCSy))
aperture = list(map(float, aperture))

#ADD DUMPL
with open(ELEMENTS_CSV_DMPL)  as csvfile:

     rows = csv.reader(csvfile, delimiter=',', quotechar='"')
     headers = next(rows)
     res = list(zip(*rows))
     # figure out when dumpline starts..
     i=0
     while len(res[0])>i and res[0][i]!='DmpL':
         i+=1
     content={}
     for h,r in zip(headers,res):
         content[h]=r[i:]

dump_index = list(content['index'])
dump_index = [v.lstrip('0') for v in dump_index]
dump_index = list(map(int, dump_index[:-1]))

section.extend(content['sect'])
essname.extend(content['essname'])
model.extend(content['model'])
slot_number.extend(content['cell'])
slot_type.extend(content['slot'])
element.extend(content['elem'])
index.extend(dump_index)
doorsid.extend(content['doorsid'])
aperture.extend(content['r[mm]'])
TCSz.extend(content['TCS,m,z[mm]'])
TCSy.extend(content['TCS,m,y[mm]'])
MCSz.extend(content['MCS,m,z[mm]'])
MCSy.extend(content['MCS,m,y[mm]'])
#print(TCSy)
#quit()



#TCSz[:] = [x - 85 for x in TCSz]

#BEGIN ENERGY CODE
with open(os.path.join(os.path.dirname(sys.argv[0]),'energies.txt'))  as csvfile:
     rows = csv.reader(csvfile, delimiter='\t')
     res = list(zip(*rows))

energyName = res[1]
energyInput = res[9]

#create list of equal length to current list, basic energy level of 0.075
numTotalElements = len(index)
numEnergyElements = len(energyInput)

currentEnergy = 0.075
elementEnergy = [None]*numTotalElements
energyElementNameList = [None]*numTotalElements

#BUILD COMPATIBLE NAME LIST FOR ENERGY
RFQ_i = 1
DTL_i = 1
Cav_i = 1

for i in range(0, numTotalElements):
    if(element[i]=="RFC"):
        energyElementNameList[i] = "RFQ" + str(RFQ_i)
        RFQ_i += 1
    elif(element[i]=="DTC"):
        energyElementNameList[i] = "DTL" + str(DTL_i)
        DTL_i += 1
    elif(element[i]=="Cav"):
        energyElementNameList[i] = "FM" + str(Cav_i)
        Cav_i += 1
    else:
        energyElementNameList[i] = "null"

#for every element in the lattice
for i in range(0, numTotalElements):
    #search for that name in the energy element list
    for j in range(0, numEnergyElements):
        #if you find the name
        if(energyElementNameList[i]==energyName[j]):
            #the element's energy is equal to the same energy index
            elementEnergy[i] = energyInput[j]
            currentEnergy = energyInput[j]
        #if you don't find the name, use the last energy
        else:
            elementEnergy[i] = currentEnergy

#END ENERGY CODE

#BEGIN PBI_SHOPPINGLIST_LINKS
with open(os.path.join(os.path.dirname(sys.argv[0]),'shoppingList.csv'))  as csvfile:
     rows = csv.reader(csvfile, delimiter=',')
     res = list(zip(*rows))

insight_ESSName = res[0]
insight_ID = res[1]

#create list of equal length to current list, basic energy level of 0.075
#numTotalElements = len(index)
numInsightElements = len(insight_ESSName)

insightLink = [None]*numTotalElements

#for every element in the lattice
for i in range(0, numTotalElements):
    #search for that name in the shopping list
    insightLink[i] = "n/a"
    for j in range(0, numInsightElements):
        #if you find the name
        if(essname[i]==insight_ESSName[j]):
            #the element's INSIGHT LINK is equal
            insightLink[i] = insight_ID[j]
            #print(insightLink[i], i);

#END PBI_SHOPPINGLIST_LINKS


# First we initialize parser objects
pLEBT = parseLEBT.LEBT()
pMEBT = parseMEBT.MEBT()
pDTL  = parseDTL.DTL()
pSPK  = parseSPK.SPK()
pMBL  = parseMBL.MBL()
pHBL  = parseHBL.HBL()
pHEBT = parseHEBT.HEBT()
pA2T  = parseA2T.A2T()
pDmpL = parseDumpL.DumpL()

for        element, essname, insightLink, section, aperture, model, index, slot_number, slot_type, doorsid, elementEnergy, TCSz, TCSy, MCSz, MCSy \
    in zip(element, essname, insightLink, section, aperture, model, index, slot_number, slot_type, doorsid, elementEnergy, TCSz, TCSy, MCSz, MCSy):
    if section in ['ISrc', 'LEBT']:
        pLEBT.append(element, essname, insightLink, model, section, aperture, index, slot_number, slot_type, elementEnergy, TCSz, TCSy, MCSz, MCSy)
    if (section == 'MEBT' or section == 'RFQ'):
        pMEBT.append(element, essname, insightLink, model, section, aperture, index, slot_number, slot_type, doorsid, elementEnergy, TCSz, TCSy, MCSz, MCSy)
    if (section == 'DTL'):
        pDTL.append(element, essname, insightLink, model, section, aperture, index, slot_number, slot_type, doorsid, elementEnergy, TCSz, TCSy, MCSz, MCSy)
    if (section == 'Spk'):
        pSPK.append(element, essname, insightLink, model, section, aperture, index, slot_number, slot_type, elementEnergy, TCSz, TCSy, MCSz, MCSy)
    if (section == 'MBL'):
        pMBL.append(element, essname, insightLink, model, section, aperture, index, slot_number, slot_type, doorsid, elementEnergy, TCSz, TCSy, MCSz, MCSy)
    if (section == 'HBL'):
        pHBL.append(element, essname, insightLink, model, section, aperture, index, slot_number, slot_type, doorsid, elementEnergy, TCSz, TCSy, MCSz, MCSy)
    if (section == 'HEBT'):
        pHEBT.append(element, essname, insightLink, model, section, aperture, index, slot_number, slot_type, elementEnergy, TCSz, TCSy, MCSz, MCSy)
    if section in ['A2T','PBW','Mnlt']:
        pA2T.append(element, essname, insightLink, model, section, aperture, index, slot_number, slot_type, doorsid, elementEnergy, TCSz, TCSy, MCSz, MCSy)
    if (section == 'DmpL'):
        pDmpL.append(element, essname, insightLink, model, section, aperture, index, slot_number, slot_type, doorsid, elementEnergy, TCSz, TCSy, MCSz, MCSy)

# After Parsing we write all files..
pLEBT.write()
pMEBT.write()
pDTL.write()
pSPK.write()
pMBL.write()
pHBL.write()
pHEBT.write()
pA2T.write()
pDmpL.write()

# If the NFS is mounted in Thomas' home directory..
# fromDirectory = r'HTML'
# toDirectory = r"C:\\newGit\\BD Viewer\\templates"
#
# if os.path.exists(toDirectory):
#     copy_tree(fromDirectory, toDirectory)

# Now we create new json files if we have downloaded info about previous files..
# for section in ['LEBT', 'RFQ-MEBT', 'DTL', 'SPK', 'MBL', 'HBL', 'HEBT', 'DumpL', 'A2T']:
#     infofile='info_{}.json'.format(section)
#     newfile=os.path.join('HTML',section,section+'.json')
#
#     if os.path.exists(infofile):
#         import json
#
#         # Read current page info/content
#         info=json.loads(open(infofile,'r').read())
#
#         # some information needed to generate new page:
#         page_id=info['id']
#         page_title=info['title']
#         space_key=info['space']['key']
#
#         version_current=info['version']['number']
#         version={'number':str(int(version_current)+1)}
#         if 'CI_COMMIT_SHA' in os.environ:
#             version['message'] = 'Automatic from {} on {}@{}'.format(
#                     os.environ['CI_COMMIT_SHA'],
#                     os.environ['CI_COMMIT_REF_NAME'],
#                     os.environ['CI_PROJECT_PATH'])
#
#         content=open(os.path.join('HTML',section,section+'.txt')).read()
#         storage={"storage": {"value": content,
#                  "representation": "storage"}}
#         data={"type":"page",
#               "title":page_title,
#               "space":{"key":space_key},
#               "version": version,
#               "body": storage,
#               }
#
#         open(newfile,'w').write(json.dumps(data,indent=2))
