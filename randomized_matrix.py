import random as rd
a1 = int(input('a1 = '))
a2 = int(input('a2 = '))
A3 = []
for i in range(a1):
    row = []
    for j in range(a2):
        row.append(rd.randint(1802,1945))
    A3.append(row)
for row in A3:
    print(row)

input('Enter to end')
        