t = int(input())

def minus(s,a,b):
    for c in s:
        if c == '0': a -= 1
        elif c == '1': b -= 1
    return a,b

def numofqs(s):
    t = 0
    for c in s:
        if c == '?': t+=1
    return t

def run():
    for i in range(int(len(s) / 2)):
        j = len(s) - i - 1

for test in range(t):
    a, b = [int(x) for x in input().split()]
    s = input()
    s = [x for x in s]
    a, b = minus(s, a, b)
    # minus all must for a b
    for i in range(int(len(s)/2)):
        j = len(s) - i - 1
        if (s[i] == '?' and s[j] != '?'):
            s[i] = s[j]
            if s[j] == '0':
                a -= 1
            else:
                b -= 1
        elif (s[j] == '?' and s[i] != '?'):
            s[j] = s[i]
            if s[i] == '0':
                a -= 1
            else:
                b -= 1
    if a<0 or b<0: print(-1)
    else:
        run()
