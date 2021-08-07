a = int(input())
b = int(input())
d1 = int(input())
d2 = int(input())
s = '{:' + str(d1) + '.' + str(d2) + 'f}'
print(s)
print(s.format(a/b))