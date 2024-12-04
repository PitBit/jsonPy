#!python
# script to search same or not same string in json files

import sys
import json

# get commad line arguments
print(sys.argv)

# Open first JSON file and returns JSON object as a dictionary
fileOne = open('in1.json')
fileOneData = json.load(fileOne)
fileOne.close()

# Open second JSON file and returns JSON object as a dictionary
fileTwo = open('in2.json')
fileTwoData = json.load(fileTwo)
fileTwo.close()

# define the data keys
Keyfirst = 'RequirePorts'
KeySecond = 'RequirePort'

fileOneDataLen = len(fileOneData[Keyfirst])
fileTwoDataLen = len(fileTwoData[Keyfirst])
print('len of fileOneData', fileOneDataLen, end=' '),
print('but len of fileOneData', fileTwoDataLen)

# compare number of keys in both files
if fileOneDataLen > fileTwoDataLen:
    DataFirst = fileOneData[Keyfirst]
    DataSecond = fileTwoData[Keyfirst]
else:
    DataFirst = fileTwoData[Keyfirst]
    DataSecond = fileOneData[Keyfirst]
    
if 'RequirePorts' in fileOneData:
    KeyCnt1 = 0
    KeyCnt2 = 0
    findingsCnt = 0
    print('--R-Ports-------------------------')
    for i in DataFirst:
        if KeySecond in DataFirst[KeyCnt1]:
            print('A',KeyCnt1, '  ', DataFirst[KeyCnt1][KeySecond])#, end=' ')
            for SecondDataCnt in DataSecond:
                if KeySecond in DataSecond[KeyCnt2]:
                    print('    B',KeyCnt2,end=' ' )
                    if DataFirst[KeyCnt1][KeySecond] == DataSecond[KeyCnt2][KeySecond]:
                        print('-> found')
                        findingsCnt+=1
                    elif DataFirst[KeyCnt1][KeySecond].lower() == DataSecond[KeyCnt2][KeySecond].lower():
                        print('-> found, but not case sensitiv', DataSecond[KeyCnt2][KeySecond])
                        findingsCnt+=1
                    else:
                        print('-> not found')
                KeyCnt2+=1
            KeyCnt2=0
            if findingsCnt == 0:
                #newIf[]
                print('new interface', DataFirst[KeyCnt1][KeySecond])
            findingsCnt=0
        else:
            print('-- WARNING: key RequirePort not found, wrong scruct?')
        KeyCnt1 += 1
else:
    print('-- no ', KeySecond, ' find')
KeyCnt1 = 0
print('----------------------------')