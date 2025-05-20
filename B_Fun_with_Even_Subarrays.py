T = int(input())

def solve(A):
    n = len(A)
    if n == 1:
        return 0
    x = A[-1]
    p = 0
    s = len(A) 
    ans = 0 
    n = n-2 
    while A:
        
        flg = 0 
        t = min(2**p,s//2)
        while A  and t:
            
            if A.pop()!=x:
                flg = 1
            t-=1
        p+=1
        if flg:
            ans+=1
    return ans


for _ in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    print(solve(A))