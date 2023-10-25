import funct as f

#input
name_time = input("Enter:\n(Name: time time...; Name: time...; Name: time...)\n=====================================\n")

#{name: time}
solveList = name_time.replace(": ", "\n").replace("; ", "\n").splitlines()
solveDict = f.solveDict(solveList)
print("=================(1)=================")
print(solveDict)

#{name: time-list}
listDict = f.listDict(solveDict)
print("=================(2)=================")
print(listDict)

#str to int
intList = f.intList(listDict)
print("=================(3)=================")
print(intList)

#fastest and slowest
fastest = f.fastest(intList)
slowest = f.slowest(intList)
print("=================(4)=================")
print(fastest)
print(slowest)

#remove fastest and slowest from intList
new_intList = f.new_intList(intList, fastest, slowest)
print("=================(5)=================")
print(new_intList)
