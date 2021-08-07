t = int(input())

def printarr(arr):
    for row in arr:
        for ele in row:
            print(ele, end='')
        print()

def printres(m,n,x,y):
    ap = a
    ap[m][n] = '*'
    ap[x][y] = '*'
    printarr(ap)

for test in range(t):
    #print('t=',test)
    n = int(input())
    a = []
    for i in range(n):
        row = []
        for x in input():
            row.append(x)
        a.append(row)

    mark1 = None
    for i in range(n):
        for j in range(n):
            if a[i][j]=='*':
                if mark1 == None:
                    mark1 = [i,j]
                else:
                    mark2 = [i,j]
    #print(mark1, mark2)
    if mark1[0] == mark2[0]:
        for i in range(n):
            if i != mark1[0]:
                printres(i,mark1[1],i,mark2[1])
                break
    elif mark1[1] == mark2[1]:
        for j in range(n):
            if j != mark1[1]:
                printres(mark1[0],j,mark2[0],j)
                break
    else:
        printres(mark1[0],mark2[1],mark2[0],mark1[1])