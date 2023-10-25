import dict_function as df

#input
name_time = input("Enter:\n(Name: time time...; Name: time...; Name: time...)\n===============================\n")

#{name: time}
solveList = name_time.replace(": ", "\n").replace("; ", "\n").splitlines()
solveDict = df.solveDict(solveList)
print(solveDict)

#{name: time-list}
listDict = df.listDict(solveDict)
print(listDict)
