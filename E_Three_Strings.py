T = int(input())
from collections import defaultdict
def solve():
    a = input()
    b = input()
    c = input()

    dp = defaultdict(lambda : float("inf"))
    dp[0,0]=0 
    for x in range(1,len(a)+1):

        dp[x,0]=int(a[x-1]!=c[x-1])+dp[x-1,0]
    for x in range(1,len(b)+1):
        dp[0,x]=int(b[x-1]!=c[x-1])+dp[0,x-1]
    for x in range(1,len(a)+1):
        for y in range(1,len(b)+1):
            if a[x-1]==c[y+x-1]:
                dp[x,y] = dp[x-1,y]
            else:
                dp[x,y] = min(dp[x,y],dp[x-1,y]+1)
            if b[y-1]==c[y+x-1]:
                dp[x,y] = min(dp[x,y],dp[x,y-1])
            else:
                dp[x,y] = min(dp[x,y],dp[x,y-1]+1)
    print(dp[len(a),len(b)])
    
    return 0
for _ in range(T):
    solve()
        

    