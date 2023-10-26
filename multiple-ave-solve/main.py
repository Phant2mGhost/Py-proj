import funct as f

#extract text from time-s.txt
file = open("time-s.txt", "r")
name_time = file.read()
print("=================(0)=================")
print(name_time)

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
slowest, initSlowest = f.slowest(intList)
print("=================(4)=================")
print(fastest)
print(slowest)

#remove fastest and slowest from intList
new_intList = f.new_intList(intList, fastest, initSlowest)
print("=================(5)=================")
print(new_intList)

#mean
mean = f.mean(new_intList)
print("=================(6)=================")
print(mean)

#ranking
print("=================(7)=================")
sort_mean = f.sort_mean(mean)
print(sort_mean)


print("==============(.......)==============")
print("|||||||||||||||||||||||||||||||||||||")
print("==============(Results)==============")

#format results
listSolves = list(intList.values())
numSolves = len(listSolves[0])

#display num of solves
print(f"=============({numSolves} Solves)=============")

for mean_key, mean_value in mean.items():
    #display name
    print(f"================({mean_key})================")
    
    #display mean
    print(f"Ao{numSolves}: {mean_value}")

    #display fastest and slowest
    print(f"Fastest: {fastest[mean_key]}")
    print(f"Slowest: {slowest[mean_key]}")

print("==============(.......)==============")
print("|||||||||||||||||||||||||||||||||||||")
print("==============(Ranking)==============")

#display ranking
rank = 1
for key in sort_mean.keys():
    print(f"{rank}: {key}")
    rank += 1
print("==============(.......)==============")
