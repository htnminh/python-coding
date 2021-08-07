t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    if a[0] != a[1]:
        if a[0] == a[2]:
            print(1+1)
        else:
            print(0+1)
    else:
        for i in range(2,n):
            if a[i] != a[0]:
                print(i+1)
                break
