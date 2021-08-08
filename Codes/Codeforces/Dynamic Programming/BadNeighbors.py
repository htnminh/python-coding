s = input().replace('{', '')
s = s.replace('}', '')
tup = eval(s)

def not_neighbor(j, i): # j < i
    if abs(i - j) == 1:
        return False
    if j == 0 and i == len(tup) - 1:
        return False
    return True


d = {0: {tup[0]}}

def max_including(i):
    if i in d:
        return d[i]
    res = tup[i]
    for j in range(i):
        if not_neighbor(j, i):
            if max_including(j) + tup[i] > res:
                res = max_including(j) + tup[i]
                print('%s = %s + %s' % (res, max_including(j), tup[i]))
    d[i] = res
    return res

print(max([max_including(i) for i in range(len(tup))]))
'''
0)		
{ 10, 3, 2, 5, 7, 8 }
Returns: 19
The maximum donation is 19, achieved by 10+2+7. It would be better to take 10+5+8 except that the 10 and 8 donations are from neighbors.
1)	  	
{ 11, 15 }
Returns: 15
2)	
{ 7, 7, 7, 7, 7, 7, 7 }
Returns: 21
3)	
{ 1, 2, 3, 4, 5, 1, 2, 3, 4, 5 }
Returns: 16
4)	
{ 94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,  
  6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
  52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72 }
Returns: 2926

'''