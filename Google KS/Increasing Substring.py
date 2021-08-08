t = int(input())
for test in range(t):
    n = int(input())
    s = input()
    res = '1'
    count = 1
    for i in range(1, n):
        if s[i-1] < s[i]:
            count += 1
            res += ' ' + str(count)
        else:
            count = 1
            res += ' ' + str(count)
    print('Case #', test+1, ': ', sep='', end='')
    print(res)

'''
2
4
ABBC
6
ABACDA

'''
