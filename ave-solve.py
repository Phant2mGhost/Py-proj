import numpy as np

#input to list
user_input = input("Enter time separated with spaces:\n")
strList = user_input.split()
intList = list(map(float, strList))

#fastest and slowest
fastest = max(intList)
slowest = min(intList)

#ave
intList.remove(fastest)
intList.remove(slowest)
ave = np.mean(intList)

#display time
solves = str(len(strList)+1)
print(f"Fastest: {fastest}")
print(f"Slowest: {slowest}")
print(f"Ao{solves}: {ave}")
