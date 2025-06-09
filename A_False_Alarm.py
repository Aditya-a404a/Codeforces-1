T  = int(input())

def solve():
    n,time = list(map(int,input().split()))

    nums = list(map(int,input().split()))

    left = -1
    right = -1
    for x in range(n):
        if nums[x]==1:
            left =x 
            break
    for x in range(n-1,-1,-1):
        if nums[x]==1:
            right = x
            break
    if (left==-1):
        print("YES")
    if (right-left+1)<=time:
        print("YES")
    else:
        print("NO")
for _ in range(T):
    solve()
