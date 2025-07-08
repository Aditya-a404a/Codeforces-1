T = int(input())

from collections import defaultdict
def solve():
    n = input()
    s = input()
    nums = [ int(x) for x in s ]
    # nums[r]+nums[r-1]+nums[r-2] + nums[l] = r-l+1 
    # p[r] - p[l-1] = r-l+1 
    # p[r] - r == p[l-1] - l+1 
    # p[r]-r-1 == p[l-1]-l
    # p[r] -> nums[0]+nums[1]+nums[2]+nums[3]..nums[r-1] 
    # p[0] -> 0
    # p[1] -> nums[0] 
    # to find [l,r)
    # p[r] = nums[0] + nums[1]....nums[r-1]
    # p[l] = nums[0] + nums[1] .. .nums[l-1]
    # to find [l,r]
    # p[r+1]-p[l]
    # p[r]-p[l] = r-l
    # p[r]-r = p[l]-l
    p = [0]
    dic = defaultdict(int)
    ans = 0
    dic[0] = 1 
    for i,x in enumerate(nums):
        p.append(p[-1]+x)
        ans+=dic[p[-1]-(i+1)]
        dic[p[-1]-(i+1)]+=1
    print(ans)
    pass

for _ in range(T):

    solve()


