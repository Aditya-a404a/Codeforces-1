T = int(input())

import heapq
from heapq import heappop,heappush,heapify
from collections import defaultdict
def solve():
    n,m = list(map(int,input().split()))

    grid = [ ]
    mx = 0
    for x in range(n):
        grid.append(list(map(int,input().split())))
        mx = max([mx]+grid[-1])
    r =  defaultdict(int)
    col = defaultdict(int)
    c = 0 
    for x in range(n):
        for y in range(m):
            if grid[x][y]==mx:
                r[x]+=1
                col[y]+=1
                c+=1
    # print(r)
    # print(col)
    # print(c)
    flg =0 
    for x in range(n):
        for y in range(m):
            if c-r[x]-col[y]+int(grid[x][y]==mx)<=0:
                flg = 1
    # print(666)
    print(mx-flg)
    return 

for _ in range(T):
    solve()
