
def ii():
    t = int(input())
    return t
def ai():
    l = list(map(int,input().split()))
    return l 
T = ii()

def good(mid):
    

def solve():
    n,k  = ai()
    a = ai()
    b = ai()
    person  = [(x,y) for (x,y) in zip(a,b)]
    left = 0 
    right = 2*10**9 + 1 
    while left<=right:
        mid = (left+right)//2
        if good(mid):
            left = mid+1
        else:
            right = mid-1 
    print(left)
    return 0 
    pass

for x in range(T):
    solve()