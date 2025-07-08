T = int(input())



def solve():

    a,l,r = list(map(int,input().split()))
    if min(l,r)<=a<=max(r,l):
        print("NO")
        return 
    else:
        print("YES")
for _ in range(T):
    solve()