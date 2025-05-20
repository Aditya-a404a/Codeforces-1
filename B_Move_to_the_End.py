T  = int(input())
from heapq import heappush, heappop
from collections import defaultdict

def check(A):

    n = len(A)
    s = 0 
    h = []
    ans = []
    for i, x in enumerate(A):
        heappush(h, (-x,i))
    for x in range(n-1,-1,-1):

        s+=A[x]
        while h and h[0][1]>=x:
            heappop(h)
        
        if h and  -h[0][0]>A[x]:
            ans.append(s-h[0][0]-A[x])
        else:
            ans.append(s)
    return ans 

for _ in range(T):
    n = int(input())

    A = list(map(int, input().split()))
    T = check(A)

    for x in T:
        print(x, end = " ")
    print()
