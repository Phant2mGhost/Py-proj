import re

uInput = input('Enter Numbers: ')

#input to list
nList = re.split(',|-|_', uInput)

#str to int
nInt_1 = [int(n) for n in nList]
print(f"Your Numbers: {nInt_1}")
nInt_2 = nInt_1[:]

#ascending
nOutput = []
while len(nInt_1) != 0:
    first_1 = nInt_1[0]
    for i in nInt_1:
        if (i < first_1):
            first_1 = i
    nOutput.append(first_1)
    nInt_1.remove(first_1)
print(f"Ascending: {nOutput}")
