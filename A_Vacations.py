from functools import cache
N = int(input())


A = list(map(int,input().split()))

@cache
def dp(index,prev):
    if index==len(A):
        return 0 
    else:
        ans = 2**32
        ans = min(ans,1+dp(index+1,-1))
        if A[index]==1:
            if prev==1:
                ans = min(ans,1+dp(index+1,-1))
            else:
                ans = min(ans,dp(index+1,1))
        if A[index]==2:
            if prev==2:
                ans = min(ans,1+dp(index+1,-1))
            else:
                ans = min(ans,dp(index+1,2))
        if A[index]==3:
            if prev!=1:
                ans = min(ans,dp(index+1,1))
            if prev!=2:
                ans = min(ans,dp(index+1,2))
        
        return ans
print(dp(0,-1))
            
            
            
                


