# https://codeforces.com/problemset/problem/1550/B

class String():
    def __init__(self, s) -> None:
        self.s = s

    def check_consecutive_equal(self, start, end) -> bool:
        # not including end
        return True if len(set(self.s[start : end])) == 1 else False
    
    def delete(self, start, end):
        # deletion not including end
        return String(self.s[ : start] + self.s[end : ])

    
class Case():
    def __init__(self, n, a, b, s) -> None:
        self.n = n
        self.a = a
        self.b = b
        self.s = String(s)
    
    def max_point(self):
        maximum = None
        
        def run(S, current_point):
            nonlocal maximum
            if S.s == '':
                if maximum is None or current_point > maximum:
                    maximum = current_point
            else:
                # if lenS.s == 1: i == 0, j in range(1,1) -> no run
                for i in range(len(S.s)):
                    for j in range(i + 1, len(S.s) + 1):
                        if S.check_consecutive_equal(i, j):
                            deleted_String = S.delete(i, j)
                            # print(S.s,'from',i,'to',j, 
                            #       deleted_String.s,current_point, file=open('test.txt', 'a'))
                            run(deleted_String, current_point + self.a * (j - i) + self.b)
                        else:
                            break
                            
                    
        run(self.s, 0)
        return maximum
    
# #                      012345
# case = Case(6, 1, -4, '100111')
# print(case.s.delete(1, 3).s)
# print(case.s.check_consecutive_equal(1, 3))
# print(case.max_point())
# St = String('0010000')
# print(St.check_consecutive_equal(0,1))

for _ in range(int(input())):
    n, a, b = [int(x) for x in input().split()]
    print(Case(n, a, b, input()).max_point())
    # print('Res =', Case(n, a, b, input()).max_point())