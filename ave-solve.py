import numpy as np

#input to str list
user_input = input("(Enter time separated with spaces)\n================================\n")
strList = user_input.split()

#str to int
dnf = "DNF"
nStrList = []
for s in strList:
    if s == dnf:
        s = "1000000"
    nStrList.append(s)
intList = list(map(float, nStrList))

#fastest and slowest
slowest = max(intList)
fastest = min(intList)

#ave
intList.remove(fastest)
intList.remove(slowest)
ave = np.mean(intList)

#display time
solves = str(len(strList))
print("================================")
print(f"Fastest: {fastest}")
print("================================")
if slowest == 1000000:
    print(f"Slowest: {dnf}")
else:
    print(f"Slowest: {slowest}")
print("================================")
print(f"Ao{solves}: {ave}")
print("================================")
