arr = [ int(x) for x in input('Nhap nhieu so vao: ').split() ]

t = 0
for num in arr:
    t += num
print('Tong =',t)