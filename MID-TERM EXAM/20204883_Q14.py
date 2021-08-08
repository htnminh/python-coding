start = int(input())
end = int(input())

while start > end:
    if start % 3 == 0:
        if start // 3 >= end:
            print(':3')
            start //= 3
    elif start - end >= 2 and start % 3 == 2:
        print('-2')
        start -= 2
    else:
        print('-1')
        start -= 1
        '''
    else:
        if start - end % 2 == 0:
            print('-2')
            start -= 2
        else:
            print('-1')
            start -= 1'''
        
'''and start // 3 >= end:
        print(':3')
        start //= 3
    elif start % 3 == 1 and start - 1 >= end:
        print('-1')
        start -= 1
    elif start - 2  >= end:
        print('-2')
        start -= 2
        
        
'''

        
