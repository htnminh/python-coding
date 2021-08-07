# Enter your code here. Read input from STDIN. Print output to STDOUT
k, m = [int(x) for x in input().split()]

val = []
siz = []

for i in range(k):
    inp = input().split()
    sz = int(inp[0])
    siz.append(sz)
    val.append([])
    for j in range(sz):
        val[i].append(int(inp[j + 1]))
            
res = 0
ite = [0] * k


def check():
    global res
    global ite
    s = 0
    for i in range(k):
        x = val[i][ite[i]]
        s = s + x * x
        s %= m
    res = max(res, s)

def attemp(i):
    global ite
    if i == k:
        check()
    else:
        for j in range(siz[i]):
            ite[i] = j
            attemp(i + 1)
            
attemp(0)
print(res)
