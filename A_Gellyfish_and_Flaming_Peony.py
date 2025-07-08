T = int(input())
import math
def solve():
    n = int(input())
    nums = list(map(int,input().split()))

    k = 0 
    for x in nums:
        k = math.gcd(k,x)
    
    nums = [ x//k for x in nums ] 
    mx = max(nums) 
    dp = [float("inf") for x in range(mx+1)]
    for x in nums:
        dp[x] = 0  
    for x in range(mx,0,-1):

        f = dp[x] 
        if f==float("inf"):
            continue
        for v in nums:
            g = math.gcd(x,v)
            dp[g]  =min(dp[g],dp[x]+1)
    ans = max(dp[1]-1, 0)
    ans+=sum( 1 for v in nums if v > 1  )
    print(ans) 
    
            




    pass

for x in range(T):

    solve()
