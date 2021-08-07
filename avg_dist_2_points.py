from math import *
from random import *

n = int(input('Number of tests = 10 ** '))
n = 10 ** n
print('Number of tests =', n)

def dist(coor):
    return sqrt((coor[0] - coor[1]) ** 2 + (coor[2] - coor[3]) ** 2)

sum_dist = 0

for i in range(n):
    coor = [uniform(0, 1) for j in range(4)]
    sum_dist += dist(coor)

print('Tested answer =', sum_dist / n)

exact_ans = (2 + sqrt(2) + 5 * log(sqrt(2) + 1)) / 15
print('Exact answer  =', exact_ans)
