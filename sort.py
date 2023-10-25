import re

uInput = input('Enter Numbers: ')

#input to list
nList = re.split(',|-|_| ', uInput)

#str to int
nInt_1 = [int(n) for n in nList]
print(f"Your Numbers: {nInt_1}")
nInt_2 = nInt_1[:]

#ascending
nOutput_1 = []
while len(nInt_1) != 0:
    first_1 = nInt_1[0]
    for i in nInt_1:
        if (i < first_1):
            first_1 = i
    nOutput_1.append(first_1)
    nInt_1.remove(first_1)
print(f"Ascending: {nOutput_1}")

#descending
nOutput_2 = []
while len(nInt_2) != 0:
    first_2 = nInt_2[0]
    for i in nInt_2:
        if (i > first_2):
            first_2 = i
    nOutput_2.append(first_2)
    nInt_2.remove(first_2)
print(f"Descending: {nOutput_2}")
