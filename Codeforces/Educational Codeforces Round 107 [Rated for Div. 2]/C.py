n, q = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

def first_pos(color):
    for index in range(len(a)):
        if a[index] == color:
            return index

def exchange(pos):
    value = a[pos]
    for i in range(pos, 0, -1):
        a[i] = a[i-1]
    a[0] = value

for color in b:
    print(first_pos(color)+1, end =' ')
    exchange(first_pos(color))