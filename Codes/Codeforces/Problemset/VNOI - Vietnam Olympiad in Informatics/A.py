class Thing():
    def __init__(self, tup) -> None:
        self.weight, self.value = tup
            

# class Total_thing():
#     def __init__(self, tup) -> None:
#         self.total_weight, self.total_value = tup

#     def __str__(self) -> str:
#         return '(%s %s)' % (self.total_weight, self.total_value)

N, MAX_WEIGHT_AVAIL = [int(x) for x in input().split()]
thing_lst = list()
for _ in range(N):
    thing_lst.append(Thing(tuple([int(x) for x in input().split()])))
    

def take_max_value_if_same_weight(a, b):
    if a.total_weight == b.total_weight:
        if a.total_value > b.total_value:
            return 

# dict of |int: set of objects|
d = {0: {0: 0}}
if thing_lst[0].weight <= MAX_WEIGHT_AVAIL:
    d[0][thing_lst[0].weight] = thing_lst[0].value


def weight_max_value_including(i):
    if i in d:
        return d[i]
    res = {0: 0}
    for j in range(i):
        for ele in weight_max_value_including(j):
            calc_weight = thing_lst[i].weight + ele
            calc_value = thing_lst[i].value + weight_max_value_including(j)[ele]
            if calc_weight <= MAX_WEIGHT_AVAIL:
                if calc_weight in res:
                    if calc_value > res[calc_weight]:                        
                        res[calc_weight] = calc_value
                else:
                    res[calc_weight] = calc_value
    d[i] = res
    return res

# print()
# for i in range(N):
#     print('%3i %3i     ' % (thing_lst[i].weight, thing_lst[i].value),
#                                weight_max_value_including(i), 
                              
#           )

print(max(value for i in range(N) for value in weight_max_value_including(i).values()) 
      )

# ! WRONG TEST CASE:
# https://viblo.asia/p/phan-2thuat-toan-quy-hoach-dong-maGK73zbKj2
'''
6 19
3 7
4 10
5 20
7 19
6 13
9 40

  3   7       3   7
  4  10       7  17
  5  20      12  37
  7  19      19  56
  6  13      18  50
  9  40      16  57
57
'''