import json

numbers = [1,2,3,4,5,6,7]

filename = 'json_files/numbers'


def saveJson(filename,data):
    with open(filename,'w') as file:
        json.dump(data,file)

def loadJson(filename):
    with open(filename) as file:
        s = json.load(file)
        return s

# saveJson(filename,numbers)

data = loadJson(filename)
print(data)