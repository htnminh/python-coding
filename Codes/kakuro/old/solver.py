# |-----|
# |   13|
# |     |
# |12   |
# |-----|

# |-----|
# |     |
# |  x  |
# |     |
# |-----|

# |-----|
# |#####|
# |#####|
# |-----|

import time

with open('input.txt', 'r') as inp_f:
    first_line = inp_f.readline().strip()
    num_col = len(first_line.split())
    
    inp_f.seek(0)
    
    num_row = 0
    board = list()
    for line in inp_f:
        num_row += 1
        board.append([-1 if ele == 'x' else\
                      int(ele) if ele == '0' else\
                      tuple([int(e) if e != 'x' else -1 for e in ele.split('-')])\
                        for ele in line.split()])
    
    print('Number of row = %s' % num_row)
    print('Number of col = %s' % num_col)
    
    for line in board:
        print(*line)


with open('blank_output.txt', 'w') as blank_out_f:
    # first line of board 
    blank_out_f.write('|-----' * num_col + '|\n')
    for row in board:
        # write = 1st line
        buffer = list()
        # = 2nd line 
        buffer2 = list()
        # = 3rd line 
        for num in row:
            if num == -1:
                blank_out_f.write('|#####')
                buffer.append('#####')
                buffer2.append('#####')
            # elif num == 0:
            #     blank_out_f.write('|     ')
            #     buffer.append('     ')
            #     buffer2.append('     ')
            elif isinstance(num, tuple): # num: (39, -1)
                char0, char1 = num
                if char0 == -1: char0 = ' '
                if char1 == -1: char1 = ' '
                blank_out_f.write('| \%3s' % char1)   
                buffer.append('  \  ')
                buffer2.append('%s' % char0 + \
                                ' ' * (3 - len(str(char0))) + '\ ')
            else: # num: 3
                blank_out_f.write('|     ')
                buffer.append('  %s  ' % num)
                buffer2.append('     ')
    
        blank_out_f.write('|\n')
        # write 2nd line
        for char in buffer:
            blank_out_f.write('|%s' % char)
        blank_out_f.write('|\n')
        # write 3rd line
        for char in buffer2:
            blank_out_f.write('|%s' % char)
        blank_out_f.write('|\n')
        # last line of row
        blank_out_f.write('|-----' * num_col + '|\n')
     
        
def check_duplicate(lst):
    d = set()
    for ele in lst:
        if ele not in d:
            d.add(ele)
        else:
            return False
    return True

def check_board_duplicate():
    pass

def check():    
    for i in range(num_row):
        for j in range(num_col):
            if isinstance(board[i][j], tuple):
                if board[i][j][0] != -1:
                    # print('row', board[i][j][0])
                    num_lst = list()
                    # zero_found = False
                    for i_loop in range(i + 1, num_row):
                        if isinstance(board[i_loop][j], int):
                            if board[i_loop][j] == -1:
                                break
                            num_lst.append(board[i_loop][j])
                        else:
                            break
                    # print(num_lst)
                    if not check_duplicate(num_lst):
                        return False
                    

                    if sum(num_lst) != board[i][j][0]:
                        return False
                        
                if board[i][j][1] != -1:
                    print('col', board[i][j][1])
                    num_lst = list()
                    # zero_found = False
                    for j_loop in range(j + 1, num_col):
                        if isinstance(board[i][j_loop], int):
                            if board[i][j_loop] == -1:
                                break                            
                            num_lst.append(board[i][j_loop])
                        else:
                            break

                    # print(num_lst)
                    
                    if not check_duplicate(num_lst):
                        return False
                    
                    
                    if sum(num_lst) != board[i][j][1]:
                        return False
    
    return True
                        
                        
def run(i, j):
    # print(i, j, end = ' ', sep = '')
    # next of the last row (completely out of the board)
    if i == num_row: 
        if check():
            for line in board:
                print(*line)
        return None
    # next of the last column
    elif j == num_col:
        run(i + 1, 0)
        return None
    # only run for 0
    elif board[i][j] != 0:
        run(i, j + 1)
        return None
    # run for 0
    else: 
        # for line in board:
        #     print(*line)
        # print()
        # time.sleep(1)
        for num in range(1, 10):
            #! fix here
            board[i][j] = num 
            # for line in board:
            #     for ele in line:
            #         if isinstance(ele, int):
            #             if ele not in {-1, 0}:
            #                 print(ele , end = ' ')
            if check():
                run(i, j + 1)
            board[i][j] = 0

run(0, 0)
print('Done!')