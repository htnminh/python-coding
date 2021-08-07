# board = [[-1, -1, -1, -1, (39, -1), (22, -1), -1, -1],
#  [-1, (11, -1), (13, -1), (-1, 7), 0, 0, -1, -1],
#  [(-1, 17), 0, 0, (12, 14), 0, 0, (15, -1), (6, -1)],
#  [(-1, 32), 0, 0, 0, 0, 0, 0, 0],
#  [-1, (12, -1), (5, 16), 0, 0, (14, 10), 0, 0],
#  [(-1, 4), 0, 0, (6, 16), 0, 0, (5, -1), (13, -1)],
#  [(-1, 31), 0, 0, 0, 0, 0, 0, 0],
#  [-1, -1, (-1, 9), 0, 0, (-1, 10), 0, 0],
#  [-1, -1, (-1, 7), 0, 0, -1, -1, -1]]

board = [[-1, -1, -1, -1, (39, -1), (22, -1), -1, -1],
 [-1, (11, -1), (13, -1), (-1, 7), 2, 5, -1, -1],
 [(-1, 17), 8, 9, (12, 14), 5, 9, (15, -1), (6, -1)],
 [(-1, 32), 3, 4, 5, 1, 8, 9, 2],
 [-1, (12, -1), (5, 16), 7, 9, (14, 10), 6, 4],
 [(-1, 4), 3, 1, (6, 16), 7, 9, (5, -1), (13, -1)],
 [(-1, 31), 9, 4, 2, 3, 5, 1, 7],
 [-1, -1, (-1, 9), 1, 8, (-1, 10), 4, 6],
 [-1, -1, (-1, 7), 3, 4, -1, -1, -1]]

num_row = 9
num_col = 8

def check_duplicate(lst):
    d = set()
    for ele in lst:
        if ele not in d:
            d.add(ele)
        else:
            return False
    return True

def check():    
    for i in range(num_row):
        for j in range(num_col):
            if isinstance(board[i][j], tuple):
                if board[i][j][0] != -1:
                    print('row', board[i][j][0])
                    num_lst = list()
                    # zero_found = False
                    for i_loop in range(i + 1, num_row):
                        if isinstance(board[i_loop][j], int):
                            if board[i_loop][j] == -1:
                                break
                            if board[i_loop][j] == 0:
                                zero_found = True
                            num_lst.append(board[i_loop][j])
                        else:
                            break
                    print(num_lst)
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
                            if board[i][j_loop] == 0:
                                zero_found = True
                            num_lst.append(board[i][j_loop])
                        else:
                            break

                    print(num_lst)
                    
                    if not check_duplicate(num_lst):
                        return False
                    
                    if sum(num_lst) != board[i][j][1]:
                        return False
    

    return True

print(check())