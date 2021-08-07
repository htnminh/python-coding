fi = open('sudoku.inp','r')

table =  [ [0 for row in range(9)] for col in range(9) ]
row = 0
col = 0

#all_lines = fi.read()

for line in fi:
    for x in line:
        if x>='0' and x<='9':
            table[row][col] = int(x)
            #print(table)
            col += 1
    row += 1
    col = 0

fi.close()

fo = open('sudoku.out','w')
tries = 0

def printresult():
    for row in table:
        s=''
        for item in row:
            s += str(item)
        fo.write(s+'\n')
        print(s)
    fo.write('Number of tries = '+ str(tries))
    print('Number of tries = '+ str(tries))
    fo.close()

def test(row,col):
    for i in range(9):
        if i!=row and table[i][col] == table[row][col] : return False
        if i!=col and table[row][i] == table[row][col] : return False
    for i in range(row - row%3, row - row%3 + 3):
        for j in range(col - col%3, col - col%3 + 3):
            if i!=row and j!=col and table[i][j] == table[row][col]: return False
    return True

def thu(row,col):
    if row==9:
        printresult()
    elif col==9:
        thu(row+1,0)
    elif table[row][col] != 0:
        thu(row,col+1)
    else:
        global tries
        tries += 1
        for a in range(1,10):
            table[row][col] = a
            if test(row,col):
                #print(row,col,'=',a)
                thu(row,col+1)
            table[row][col] = 0

thu(0,0)