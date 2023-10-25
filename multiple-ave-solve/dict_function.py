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
