import dict_function as df

#input
name_time = input("Enter:\n(Name: time time...; Name: time...; Name: time...)\n=====================================\n")

#{name: time}
solveList = name_time.replace(": ", "\n").replace("; ", "\n").splitlines()
solveDict = df.solveDict(solveList)
print("=================(1)=================")
print(solveDict)

#{name: time-list}
listDict = df.listDict(solveDict)
print("=================(2)=================")
print(listDict)

#str to int
intList = df.intList(listDict)
print("=================(3)=================")
print(intList)

#fastest and slowest
fastest = {}
slowest = {}
for key, value in intList.items():
    fastest[key]  = min(value)
    slowest[key]  = max(value)
print("=================(4)=================")
print(fastest)
print(slowest)

#remove fastest and slowest from intList
new_intList = df.new_intList(intList, fastest, slowest)
print("=================(5)=================")
print(new_intList)
