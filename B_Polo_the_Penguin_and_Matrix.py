n,m ,k = list(map(int,input().split()))

grid = []
for x in range(n):
    grid.append(list(map(int,input().split())))

c = grid[0][0]%k
arr=[]
for x in range(len(grid)):
    flg = 0 
    for y in range(len(grid[0])):
        arr.append(grid[x][y])
        if grid[x][y]%k!=c:
            
            flg=1
            break
    if flg:
        print(-1)
        break
else:
    arr.sort()
    ans = 0 
    t = arr[(n*m)//2]
    for x in arr:
        ans+=abs(x-t)
    ans//=k
    print(ans)


