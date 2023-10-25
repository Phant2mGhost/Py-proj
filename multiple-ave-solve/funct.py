import numpy as np

def solveDict(solveList):
    solveDict = {}
    for i in range(0, len(solveList),2):
        solveDict[solveList[i]] = solveList[i+1]
    return solveDict

def listDict(solveDict):
    listDict = {}
    dnf = "DNF"
    DNF = "1000000"
    for key, value in solveDict.items():
        listDict[key] = value.replace(dnf, DNF).split()
    return listDict

def intList(listDict):
    intList = {}
    for key, value in listDict.items():
        intList[key] = list(map(float, value))
    return intList

def fastest(intList):
    fastest = {}
    for key, value in intList.items():
        fastest[key] = min(value)
    return fastest

def slowest(intList):
    slowest = {}
    for key, value in intList.items():
        slowest[key] = max(value)
    for key, value in slowest.items():
        if value == 1000000.0:
            slowest[key] = "DNF"
        else:
            slowest[key] = value
    return slowest

def new_intList(intList, fastest, slowest):
    new_intList = {}
    for key, values in intList.items():
        copy_values = values[:]
        for value in values:
            if value in fastest.values() or value in slowest.values():
                copy_values.remove(value)
        new_intList[key] = copy_values
    return new_intList

def mean(new_intList):
    mean = {}
    for key, values in new_intList.items():
        mean[key] = np.mean(values)
    return mean

