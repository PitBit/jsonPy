#!python
# script to search same or not same string in json files
# ToDo: print messages, only by changes!

import sys
import json

# get commad line arguments
if len(sys.argv) > 1:
    fileOneName = sys.argv[1]
    if len(sys.argv)>2:
        fileTwoName = sys.argv[2]
    else:
        fileTwoName = sys.argv[1]+'_lib.json'
    print(fileOneName, fileTwoName)
else:
    fileOneName = 'file1.json'
    fileTwoName = 'file1_lib.json'

# define dict for results
result={"Modul":""}, {"key":"test"}

# Open first JSON file and returns JSON object as a dictionary
# it want to be master file
fileOne = open(fileOneName)
fileOneData = json.load(fileOne)
fileOne.close()

# Open second JSON file and returns JSON object as a dictionary
fileTwo = open(fileTwoName)
fileTwoData = json.load(fileTwo)
fileTwo.close()

print('\n--START------------------------------------------------------------------------------------------')
print(' compare files: \n    -> ', fileOneName,'\n    -> ', fileTwoName, '\n\n')

def compareKeys(key):
    MsgCnt = 0
    KeyCnt1 = 0
    KeyCnt2 = 0
    findingsCnt = 0
    firstFinding = 0
    print('----',key,': compare ', len(DataFirst),' and ', len(DataSecond),)
    while KeyCnt1 < len(DataFirst):
        # check for key in dict
        if key in DataFirst[KeyCnt1]:
            while KeyCnt2 < len(DataSecond):
                # check for key in dict
                if key in DataSecond[KeyCnt2]:
                    # compare the names
                    if DataFirst[KeyCnt1][key] == DataSecond[KeyCnt2][key]:
                        findingsCnt+=1
                    elif DataFirst[KeyCnt1][key].lower() == DataSecond[KeyCnt2][key].lower():
                        print('    -> case sensitiv\n         ',DataFirst[KeyCnt1][key],' != ', DataSecond[KeyCnt2][key])
                        MsgCnt+=1
                        findingsCnt+=1
                KeyCnt2+=1
            KeyCnt2=0
            if findingsCnt == 0:
                if firstFinding == 0:
                    print('    -> new:')
                    firstFinding=1
                print('        ', DataFirst[KeyCnt1][key])
                MsgCnt+=1
            findingsCnt=0
        else:
            print('-- WARNING: key ', key, ' not found, wrong scruct?')
        KeyCnt1 += 1
    KeyCnt1 = 0
    KeyCnt2 = 0
    findingsCnt = 0
    firstFinding = 0
    # print('    -> deleted:')
    while KeyCnt2 < len(DataSecond):
        if key in DataSecond[KeyCnt2]:
            while KeyCnt1 < len(DataFirst):
                if DataFirst[KeyCnt1][key] != DataSecond[KeyCnt2][key]:
                    if DataFirst[KeyCnt1][key].lower() != DataSecond[KeyCnt2][key].lower():
                        findingsCnt+=1
                KeyCnt1+=1
            KeyCnt1 = 0
            if findingsCnt == len(DataFirst):
                if firstFinding == 0:
                    print('    -> deleted:')
                    firstFinding=1
                print('        ', DataSecond[KeyCnt2][key])
                MsgCnt+=1
            findingsCnt = 0
        KeyCnt2+=1
    # if MsgCnt > 0:
    #     print('\n', MsgCnt, '\n')
    print('----',key,' done\n')
#-----------------------------------------------------------------------------------------------------------

# define the data keys
Keyfirst = 'RequirePorts'
KeySecond = 'RequirePort'

if Keyfirst in fileOneData:
    DataFirst = fileOneData[Keyfirst]
    DataSecond = fileTwoData[Keyfirst]
    compareKeys(KeySecond)
else:
    print('----', Keyfirst, ' key not found!')

# define the data keys
Keyfirst = 'ProvidePorts'
KeySecond = 'ProvidePort'

if Keyfirst in fileOneData:
    DataFirst = fileOneData[Keyfirst]
    DataSecond = fileTwoData[Keyfirst]
    compareKeys(KeySecond)
else:
    print('---- ', Keyfirst, ' key not found!')

# define the data keys
Keyfirst = 'CalibrationParameters'
KeySecond = 'CalibrationParameter'

if Keyfirst in fileOneData:
    DataFirst = fileOneData[Keyfirst]
    DataSecond = fileTwoData[Keyfirst]
    compareKeys(KeySecond)
else:
    print('---- ', Keyfirst, ' key not found!')
    
# define the data keys
Keyfirst = 'ParameterRequirePorts'
KeySecond = 'ParameterRequirePort'

if Keyfirst in fileOneData:
    DataFirst = fileOneData[Keyfirst]
    DataSecond = fileTwoData[Keyfirst]
    compareKeys(KeySecond)
else:
    print('---- ', Keyfirst, ' key not found!')
    
# define the data keys
Keyfirst = 'ParameterLUT'
KeySecond = 'LUTs_and_Maps'

if Keyfirst in fileOneData:
    DataFirst = fileOneData[Keyfirst]
    DataSecond = fileTwoData[Keyfirst]
    compareKeys(KeySecond)
else:
    print('---- ', Keyfirst, ' key not found!')

print('--END--------------------------------------------------------------------------------------------')
#EOF