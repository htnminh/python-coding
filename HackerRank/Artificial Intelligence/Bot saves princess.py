#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]=='m': mrow,mcol = row,col
            elif grid[row][col]=='p': prow,pcol = row,col
    if mrow < prow:
        for i in range(prow-mrow): print('DOWN')
    else:
        for i in range(mrow-prow): print('UP')
            
    if mcol < pcol:
        for i in range(pcol-mcol): print('RIGHT')
    else:
        for i in range(mcol-pcol): print('LEFT')

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)