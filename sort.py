import re

uInput = input('Enter Nynbers: ')

#input to list
nList = re.split(',|-|_', uInput)

#str to int
nInt = [int(n) for n in nList]
print(f"Your Numbers: {nInt}")
