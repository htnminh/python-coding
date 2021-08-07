# https://codeforces.com/problemset/problem/266/B

length, time = [int(x) for x in input().split()]
lst = [x for x in input()]
check_lst = [True for i in range(length)]

try:
    first_boy_pos = lst.index('B')
    
    for _ in range(time):
        for i in range(first_boy_pos, length - 1):
            if lst[i] == 'B' and lst[i + 1] == 'G'\
              and check_lst[i] and check_lst[i + 1]:
                lst[i] = 'G'
                lst[i + 1] = 'B'
                check_lst[i] = False
                check_lst[i + 1] = False
                # print(''.join(lst))
                # print(check_lst)
        first_boy_pos = lst.index('B')
        check_lst = [True for i in range(length)]
    
except ValueError:
    pass

print(''.join(lst))
