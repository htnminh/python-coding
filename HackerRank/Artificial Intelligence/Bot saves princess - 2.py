#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]=='m': mrow,mcol = row,col
            elif grid[row][col]=='p': prow,pcol = row,col
    if mrow < prow:
        print('DOWN')
    elif mrow > prow:
        print('UP')
            
    elif mcol < pcol:
        print('RIGHT')
    else:
        print('LEFT')

m = int(input())
x,y = [x for x in input().split()]
grid = []
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
