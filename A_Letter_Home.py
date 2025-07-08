T =  int(input())

def solve():

    n,s = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    
    nums.sort()
    if s <= nums[0]:
        print(nums[-1]-s)
        return 
    if s >=nums[-1]:
        print(abs(nums[0]-s))
        return
    if nums[0]<s<nums[-1]:

        mi = min(abs((s-nums[0])*2+nums[-1]-s),abs((nums[-1]-s)*2+abs(nums[0]-s)))
        print(mi)
        return
for _ in range(T):
    solve()



    
