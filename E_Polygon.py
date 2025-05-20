T = int(input())

def check(grid):

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == '1':
                s = 2 
                if y+1<len(grid) and grid[x][y+1] == '0':
                    s-=1
                if x+1<len(grid) and grid[x+1][y] == '0':
                    s-=1
                if s==0:
                    
                    return "NO"
    return "YES"
                
                
                    


    


    pass


for _ in range(T):

    N = int(input())
    grid = []
    for i in range(N):
        grid.append(list(input()))
    print(check(grid))
