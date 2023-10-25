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

def new_intList(intList, fastest, slowest):
    new_intList = {}
    for key, values in intList.items():
        copy_values = values[:]
        for value in values:
            if value in fastest.values() or value in slowest.values():
                copy_values.remove(value)
        new_intList[key] = copy_values
    return new_intList
