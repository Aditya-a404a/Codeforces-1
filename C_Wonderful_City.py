T = int(input())

def solve(grid,n,a):

    inf = 10**18
    dp = [ [inf]*2 for x in range(n)]
    dp[0][0] = 0
    dp[0][1] = a[0]

    for x in range(1,n):
        for i in range(2):
            for j in range(2):
                ok = True
                for y in range(n):
                    if grid[x][y]+i==grid[x-1][y]+j:

                        ok = False
                        break
                if ok:
                    if i ==0:
                        dp[x][i] = min(dp[x][i],dp[x-1][j])
                    else:
                        dp[x][i] = min(dp[x][i],dp[x-1][j]+a[x])
    return min(dp[-1][0],dp[-1][1])

            


    


for _ in range(T):
    inf = 10**18
    n = int(input())
    grid = [ ]
    for x in range(n):
        grid.append(list(map(int,input().split())))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    T = [ list(x) for x in zip(*grid)]
    t = (solve(grid,n,A)+solve(T,n,B))
    if t>=inf:
        print(-1)
    else:
        print(t)

