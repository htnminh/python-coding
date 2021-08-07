x=int(input("Nhập số cần tính giai thừa: "))

def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)
print (str(x)+"! =",fact(x))

gt=1
for i in range(1,x+1):
    gt = gt* i
print(gt)