T  = int(input())

def check(a,b):

    s = sum(a)
    s1 = 0 
    ans = 2**32 
    worst = 0
    
    for i in range(len(a)):
        s-=a[i]
        worst = max(s,s1)
        ans = min(ans,worst)
        s1+=b[i]
    return ans


    pass

for _ in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    print(check(a,b))

