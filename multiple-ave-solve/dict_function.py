def solveDict(solveList):
    solveDict = {}
    for i in range(0, len(solveList),2):
        solveDict[solveList[i]] = solveList[i+1]
    return solveDict

def listDict(solveDict):
    listDict = {}
    for key, value in solveDict.items():
        listDict[key] = value.split()
    return listDict
