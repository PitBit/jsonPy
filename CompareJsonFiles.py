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
#
# ToDo:
# (-) fill the delete elements
# (-) add git script information
# (-) create JSON file for output
# (-) define JSON template for output
# (-) catch the eeror by "Doesn't exist"

import sys
import json
import datetime
#import git

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

# delete key "deleted"
fileOneData.pop('deleted', None)

# Open second JSON file and returns JSON object as a dictionary
fileTwo = open(fileTwoName)
fileTwoData = json.load(fileTwo)
fileTwo.close()

if not 'Script' in fileOneData:
    fileOneData['Script']={}
fileOneData['Script']['CompareJsonFile']={'time':'datetime.datetime.now()'}

print('\n--START------------------------------------------------------------------------------------------')
print(' compare files: \n    -> ', fileOneName,'\n    -> ', fileTwoName, '\n')

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
                if findingsCnt == 0:
                    if firstFinding == 0:
                        print('    -> new:')
                        firstFinding=1
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
                    # create sctuct for deleted interfaces
                    if firstFinding == 0:
                        print('    -> deleted:')
                        firstFinding=1
                    if not 'deleted' in fileOneData:
                        fileOneData['deleted'] = {key1:[]}
                    if not key1 in fileOneData['deleted']:
                        fileOneData['deleted'][key1]=[]
                    if not key in fileOneData['deleted'][key1]:
                        fileOneData['deleted'][key1].append({key:fileTwoData[key1][KeyCnt2][key]})
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
fileOneS = open(fileOneName, 'w')
json.dump(fileOneData, fileOneS, ensure_ascii=False, indent=4)
fileOneS.close()

print('--END--------------------------------------------------------------------------------------------')
#EOF