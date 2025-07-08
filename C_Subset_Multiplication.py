T = int(input())
import math
def solve():
    n = int(input())
    nums = list(map(int,input().split()))
    pairs = [ ]
    for x in range(len(nums)-1):
        if nums[x+1]%nums[x]!=0:
            g = math.gcd(nums[x+1],nums[x])
            pairs.append((nums[x]//g,x,x+1))
    pro = 1 
    seen = set()
    for x in pairs:
        if x[0] not in seen:
            pro*=x[0]
            seen.add(x[0])
    print(pro)

for _ in range(T):
    solve()
