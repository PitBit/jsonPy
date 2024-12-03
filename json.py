# script to search same or not same string in json files

import json

# Open first JSON file and returns JSON object as a dictionary
fileOne = open('in1.json')
fileOneData = json.load(fileOne)
fileOne.close()

# Open second JSON file and returns JSON object as a dictionary
fileTwo = open('in2.json')
fileTwoData = json.load(fileTwo)
fileTwo.close()

# check json classes in data
if 'RequirePorts' in fileOneData:
    counter = 0
    findingsCnt = 0
    print('--R-Ports--file-1-----------------------')
    for i in fileOneData['RequirePorts']:
        if 'RequirePort' in fileOneData['RequirePorts'][counter]:
            print(fileOneData['RequirePorts'][counter]['RequirePort'])
        else:
            print('-- WARNING: key RequirePort not found, wrong scruct?')
        counter += 1
else:
    print('-- no Require Ports find')
if 'ProvidePorts' in fileOneData:
    counter = 0
    print('--R-Ports--file-2-----------------------')
    for i in fileOneData['RequirePorts']:
        if 'RequirePort' in fileOneData['RequirePorts'][counter]:
            print(fileOneData['RequirePorts'][counter]['RequirePort'])
        else:
            print('-- WARNING: key ProvidePort not found, wrong scruct?')
        counter = counter + 1
print('----------------------------')