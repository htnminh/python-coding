def ngto (a):
    if a<2: return False
    for i in range(2, int(a**(1/2))+1):
        if a%i==0: return False
    return True

def min_ngto_of (c):
    if c<=0:
        return 1
    for i in range(int(10**(c-1)+1), int(10**c)):
        if ngto(i):
            return i

t = int(input())

for test in range(t):
    a, b, c = [int(x) for x in input().split()]

    if a == b:
        #print('t ', min_ngto_of(c),  min_ngto_of(a-c+1), min_ngto_of(c) , min_ngto_of(b-c+1) , min_ngto_of(c))
        print(min_ngto_of(c) * min_ngto_of(a-c+1), min_ngto_of(c) * min_ngto_of(b-c+1) + min_ngto_of(c))
    else:
        print(min_ngto_of(c) * min_ngto_of(a - c +1), min_ngto_of(c) * min_ngto_of(b - c+1))
        #print((10 ** (c - 1) + 1) * min_ngto_of(a), (10 ** (c - 1) + 1) * min_ngto_of(b))