import sys
input = sys.stdin.readline
from collections import defaultdict

T = int(input())

def solve(nums,k):
    dic = defaultdict(int)
    c = 0 
    s = 0 
    mx =0 
    l = 0
    for i,x in enumerate(nums):
        if s <=0:
            c = 0
            s = 0
            l = i 
            dic = defaultdict(int)
        dic[x]+=1
        if dic[x]==1:
            c+=1
        s+=x
        while l < i and ( c > k or nums[l]<0):
            dic[nums[l]]-=1
            if dic[nums[l]]==0:
                c-=1
            s-=nums[l]
            if s<=0:
                s = x
                c = 1
                l = i 
                while lcdscscps p,d op,dpl ,dpc ,w[dc ,[d [d, [,d[ s[x ,[pwd, -p[dw, [p,d[pc,1e-v,-e1v,-,-,1e=pw,1wpel,]]]]]]]]]]
            l+=1
        mx = max(mx,s)
    return mx 

    
