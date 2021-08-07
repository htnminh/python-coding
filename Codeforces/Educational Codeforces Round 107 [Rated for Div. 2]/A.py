t = int(input())

def other(num):
    if num == 0: return 1
    else: return 0

def apply(crv, revt, sv, crup):
    if revt == 1:
        crv[sv] += 1
        return crv, crup + 1
    elif revt == 2:
        crv[sv] -= 1
        return crv, crup
    else:
        if crv[sv] < crv[other(sv)]:
            crv[sv] -= 1
            return crv, crup
        else:
            crv[sv] += 1
            return crv, crup + 1

for test in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]

    crv = [0, 0]; crup = 0
    for revt in a:
        if crv[0] == crv[1]: crv, crup = apply(crv, revt, 0, crup)
        elif crv[0] < crv[1]:
            if revt == 1: crv, crup = apply(crv, revt, 0, crup)
            elif revt == 2: crv, crup = apply(crv, revt, 1, crup)
            else: crv, crup = apply(crv, revt, 1, crup)
        else:
            if revt == 1: crv, crup = apply(crv, revt, 1, crup)
            elif revt == 2: crv, crup = apply(crv, revt, 0, crup)
            else: crv, crup = apply(crv, revt, 0, crup)
    print(crup)