n = int(input('n = '))
x = []; y = []
for i in range(n):
    val_x = float(input('x = '))
    val_y = float(input('p (' + str(val_x) + ') = '))
    x.append(val_x); y.append(val_y)
cal_x = float(input('Calculate at x = '))
res = 0
for i in range(n):
    t = y[i]
    for j in range(n):
        if j != i:
            t *= (cal_x - x[j]) / (x[i] - x[j])
    res += t
print(res)