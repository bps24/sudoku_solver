import numpy as np
grid2=[  [5,3,4,6,7,8,9,1,2],
        [6,7,2,1,9,5,3,4,8],
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1],
        [7,1,3,9,2,4,8,5,6],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],]

grid=[  [8,0,0,0,0,0,0,0,0],
        [0,0,3,6,0,0,0,0,0],
        [0,7,0,0,9,0,2,0,0],
        [0,5,0,0,0,7,0,0,0],
        [0,0,0,0,4,5,7,0,0],
        [0,0,0,1,0,0,0,3,0],
        [0,0,1,0,0,0,0,6,8],
        [0,0,8,5,0,0,0,1,0],
        [0,9,0,0,0,0,4,0,0],]

def possible(y,x,n):
    global grid 
    for i in range(9):
        if grid[y][i]==n:
            return False
    for i in range(9):
        if grid[i][x]==n:
            return False
    for i in range(3):
        for j in range(3):
            if grid[((y//3)*3)+i][((x//3)*3)+j]==n:
                return False
    return True

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x]==0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x]=n
                        solve()
                        grid[y][x]=0
                return
    print(np.matrix(grid))

    

print("solving")
solve()
    
    
