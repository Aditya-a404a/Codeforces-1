T = int(input())
from collections import defaultdict

def check(pairs,n):
    inf = 2**32 
    mi = [-1]*n

    for x,y in pairs:
        x , y = max(x,y),min(x,y)
        mi[x]=max(mi[x],y)
    
    ans = 0 
    m = -1
    
    for x in range(n):
        m  = max(m,mi[x])
        ans+=(x-m)
    print(ans)


        


    pass

for _ in range(T):

    n,m = list(map(int,input().split()))
    pair = [] 
    for x in range(m):
        pair.append(list(map(lambda x: int(x)-1,input().split())))
    check(pair,n)
    


