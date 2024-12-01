# script to search same or not same string in json files

import json

# Opening JSON file
fileOne = open('in1.json')

# returns JSON object as a dictionary
data = json.load(fileOne)
fileOne.close()

#read second file to compare
fileTwo = open('in2.json')
fileTwoData = json.load(fileTwo)
fileTwo.close()

# Iterating through the json list
count = 0
for i in data['inports']:
    print(data['inports'][count]['inport'])
    count = count + 1
print('----------------------------')
count = 0
for i in data['outports']:
    print(data['outports'][count]['outport'])
    count = count+1
print('----------------------------')