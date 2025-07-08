n,t  = list(map(int,input().split()))

nums = list(map(int,input().split()))

l= 0 
ans = 0 
s = 0
for r in range(len(nums)):
    s+=nums[r]
    while l<=r and s > t:
        s-=nums[l]
        l+=1
    ans = max(ans,r-l+1)
print(ans)
        
