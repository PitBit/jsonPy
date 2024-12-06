#!python
# script to search same or not same string in json files

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
    fileOneName = 'in1.json'
    fileTwoName = 'in2.json'

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

print('\n-------------------------------------------------------------------------------------------------')
print(' Master File: ', fileOneName,' will be compare with old file: ', fileTwoName)

def compareKeys(key):
    KeyCnt1 = 0
    KeyCnt2 = 0
    findingsCnt = 0
    print('--',key,'-compare--------------------------------------------------------------------------')
    while KeyCnt1 < len(DataFirst):
        lastFind =''
        # check for key in dict
        if key in DataFirst[KeyCnt1]:
            while KeyCnt2 < len(DataSecond):
                # check for key in dict
                if key in DataSecond[KeyCnt2]:
                    # compare the names
                    if DataFirst[KeyCnt1][key] == DataSecond[KeyCnt2][key]:
                        findingsCnt+=1
                        lastFind = DataFirst[KeyCnt1][key]
                    elif DataFirst[KeyCnt1][key].lower() == DataSecond[KeyCnt2][key].lower():
                        print('    -> case sensitiv\n         ',DataFirst[KeyCnt1][key],' != ', DataSecond[KeyCnt2][key])
                        findingsCnt+=1
                KeyCnt2+=1
            KeyCnt2=0
            if findingsCnt == 0:
                print('    -> new interface: \n        ', DataFirst[KeyCnt1][key])
            elif findingsCnt > 1:
                print('    -> double declaration, please check this: ', lastFind)
            findingsCnt=0
        else:
            print('-- WARNING: key RequirePort not found, wrong scruct?')
        KeyCnt1 += 1
    KeyCnt1 = 0
    KeyCnt2 = 0
    findingsCnt = 0
    print('    -> deleted:')
    while KeyCnt2 < len(DataSecond):
        if key in DataSecond[KeyCnt2]:
            while KeyCnt1 < len(DataFirst):
                if DataFirst[KeyCnt1][key] != DataSecond[KeyCnt2][key]:
                    if DataFirst[KeyCnt1][key].lower() != DataSecond[KeyCnt2][key].lower():
                        findingsCnt+=1
                KeyCnt1+=1
            KeyCnt1 = 0
            if findingsCnt == len(DataFirst):
                print('        ', DataSecond[KeyCnt2][key])
            findingsCnt = 0
        KeyCnt2+=1
    print('--',key,'-END------------------------------------------------------------------------------\n')

# define the data keys
Keyfirst = 'RequirePorts'
KeySecond = 'RequirePort'

DataFirst = fileOneData[Keyfirst]
DataSecond = fileTwoData[Keyfirst]

if Keyfirst in fileOneData:
    compareKeys(KeySecond)
else:
    print('-- no ', Keyfirst, ' find')

# define the data keys
Keyfirst = 'ProvidePorts'
KeySecond = 'ProvidePort'

DataFirst = fileOneData[Keyfirst]
DataSecond = fileTwoData[Keyfirst]

if Keyfirst in fileOneData:
    compareKeys(KeySecond)
else:
    print('-- no ', Keyfirst, ' find')

# define the data keys
Keyfirst = 'CalibrationParameters'
KeySecond = 'CalibrationParameter'

DataFirst = fileOneData[Keyfirst]
DataSecond = fileTwoData[Keyfirst]

if Keyfirst in fileOneData:
    compareKeys(KeySecond)
else:
    print('-- no ', Keyfirst, ' find')
    
# define the data keys
Keyfirst = 'ParameterRequirePorts'
KeySecond = 'ParameterRequirePort'

DataFirst = fileOneData[Keyfirst]
DataSecond = fileTwoData[Keyfirst]

if Keyfirst in fileOneData:
    compareKeys(KeySecond)
else:
    print('-- no ', Keyfirst, ' find')
    