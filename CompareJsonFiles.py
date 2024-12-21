#!python
# script to search same or not same string in json files
# Done:
# (x) read both files
# (x) get filename as argument
# (x) find new  interfaces
# (x) find deleted interfaces
# (x) find case sensitiv names
# (x) update json for status with same name
# (x) update json for case sensetiv
# (x) update json for deleted interfaces
# (x) fill the delete elements
# (x) fill the delete elements
# (x) catch the state of deleted interfaces
#
# ToDo:
# (-) add git script information
# (-) create JSON file for output ->20241220 I think we don´t need this
# (-) define JSON template for output
# (-) catch the eeror by "Doesn't exist", all information are inside...
# (-) report master file as excel file

import sys
import json
import datetime
#import git

# enable write new interfaces to json file as own key
writeNewIf2Json = False
# enable  write delete interfaces to json file as own key
writeDelIf2Json = False
# enable write delete interfaces to same key in json file
writeDelIf2KeyInJson = True

# get commad line arguments
if len(sys.argv) > 1:
    fileOneName = sys.argv[1]
    if len(sys.argv)>2:
        fileTwoName = sys.argv[2]
    else:
        fileTwoName = sys.argv[1]+'_lib.json'
    print(fileOneName, fileTwoName)
else:
    fileOneName = 'file1_lib.json'
    fileTwoName = 'file1.json'

# Open first JSON file and returns JSON object as a dictionary
# it want to be master file
fileOne = open(fileOneName)
fileOneData = json.load(fileOne)
fileOne.close()

# delete key section "Deleted"
if 'Deleted' in fileOneData:
    fileOneData.pop('Deleted', None)

# delete key section "New"
if 'New' in fileOneData:
    fileOneData.pop('New', None)

# Open second JSON file and returns JSON object as a dictionary
fileTwo = open(fileTwoName)
fileTwoData = json.load(fileTwo)
fileTwo.close()

if not 'Script' in fileOneData:
    fileOneData['Script']={}

datetimenow = str(datetime.datetime.now())
fileOneData['Script']['CompareJsonFile'] = {'description':'This script compare two different JSON Files, new and old file, with Matlab Model interface description'}
fileOneData['Script']['CompareJsonFile']['time'] = datetimenow
fileOneData['Script']['CompareJsonFile']['newFile'] = fileOneName
fileOneData['Script']['CompareJsonFile']['oldFile'] = fileTwoName

print('\n--START------------------------------------------------------------------------------------------')
print(' compare files: \n    -> ', fileOneName,'\n    -> ', fileTwoName, '\n')

#------------------------------------------------------------------------------------------------
# function for compare file data
# parameter: key1=first key in json file,
# global prameter: writeNewIf2Json, writeDelIf2Json, writeDelIf2KeyInJson
# global data: fileOneData, fileOneData
#
def compareKeys(key1, key):
    # check if key available in file data
    if key1 in fileOneData:
        KeyCnt1 = 0
        KeyCnt2 = 0
        findingsCnt = 0
        firstFinding = 0
        print('----',key,': compare ', len(fileOneData[key1]),' and ', len(fileTwoData[key1]),)
        while KeyCnt1 < len(fileOneData[key1]):
            # check for key in dict
            if key in fileOneData[key1][KeyCnt1]:
                while KeyCnt2 < len(fileTwoData[key1]):
                    # check for delete state, dont compare this element
                    if fileOneData[key1][KeyCnt1]['state'] != 'deleted':
                        # check for key in dict
                        if key in fileTwoData[key1][KeyCnt2]:
                            # compare the names
                            if fileOneData[key1][KeyCnt1][key] == fileTwoData[key1][KeyCnt2][key]:
                                findingsCnt+=1
                                fileOneData[key1][KeyCnt1]['state'] = 'compared'
                            elif fileOneData[key1][KeyCnt1][key].lower() == fileTwoData[key1][KeyCnt2][key].lower():
                                print('    -> case sensitiv\n         ',fileOneData[key1][KeyCnt1][key],' != ', fileTwoData[key1][KeyCnt2][key])
                                fileOneData[key1][KeyCnt1]['state'] = 'check_4_case_sensitiv'
                                findingsCnt+=1
                    KeyCnt2+=1
                KeyCnt2=0
                if findingsCnt == 0 and fileOneData[key1][KeyCnt1]['state'] != 'deleted':
                    if firstFinding == 0:
                        print('    -> new:')
                        firstFinding=1

                    # create new section 'New' and write
                    if writeNewIf2Json:
                        if not 'New' in fileOneData:
                            fileOneData['New'] = {key1:[]}
                        if not key1 in fileOneData['New']:
                            fileOneData['New'][key1]=[]
                        if not key in fileOneData['New'][key1]:
                            fileOneData['New'][key1].append({key:fileTwoData[key1][KeyCnt2][key]})
                    #
                    print('        ', fileOneData[key1][KeyCnt1][key])
                    fileOneData[key1][KeyCnt1]['state'] = 'new'
                findingsCnt=0
            else:
                print('-- WARNING: key ', key, ' not found, wrong scruct?')
            KeyCnt1 += 1
        KeyCnt1 = 0
        KeyCnt2 = 0
        findingsCnt = 0
        firstFinding = 0
        deletedIfCnt = 0
        # use data fron second file to see what was deleted
        while KeyCnt2 < len(fileTwoData[key1]):
            if key in fileTwoData[key1][KeyCnt2]:
                while KeyCnt1 < len(fileOneData[key1]):
                    if fileOneData[key1][KeyCnt1][key] != fileTwoData[key1][KeyCnt2][key]:
                        if fileOneData[key1][KeyCnt1][key].lower() != fileTwoData[key1][KeyCnt2][key].lower():
                            findingsCnt+=1
                    KeyCnt1+=1
                KeyCnt1 = 0
                if findingsCnt == len(fileOneData[key1]):
                    if firstFinding == 0:
                        print('    -> Deleted:')
                        firstFinding=1

                    # create sctuct for deleted interfaces
                    if writeDelIf2Json:
                        if not 'Deleted' in fileOneData:
                            fileOneData['Deleted'] = {key1:[]}
                        if not key1 in fileOneData['Deleted']:
                            fileOneData['Deleted'][key1]=[]
                        if not key in fileOneData['Deleted'][key1]:
                            fileOneData['Deleted'][key1].append({key:fileTwoData[key1][KeyCnt2][key]})
                    #
                    # write deleted elements into key (append)
                    if writeDelIf2KeyInJson:
                        print('')
                        fileOneData[key1].append({key:fileTwoData[key1][KeyCnt2][key]})
                        fileOneData[key1][findingsCnt]['state'] = 'deleted'

                    print('        ', fileTwoData[key1][KeyCnt2][key])
                    deletedIfCnt+=1
                findingsCnt = 0
            KeyCnt2+=1
        print('\n') #print('----', key,' done\n')
        # print(tempData)
    else:
        print('----', key1, ' key not found!')
#-----------------------------------------------------------------------------------------------------------

compareKeys('RequirePorts', 'RequirePort')
compareKeys('ProvidePorts', 'ProvidePort')
compareKeys('CalibrationParameters','CalibrationParameter')
compareKeys('ParameterRequirePorts', 'ParameterRequirePort')
compareKeys('ParameterLUT', 'LUTs_and_Maps')

# g = git.Git('/./') 
# hexshas = g.log('--pretty=%H','--follow','--',filename).split('\n') 
# print(hexshas)

# store changed json into file
fileOne = open(fileOneName, 'w')
json.dump(fileOneData, fileOne, ensure_ascii=False, indent=4)
fileOne.close()

print('--END--------------------------------------------------------------------------------------------')
#EOF