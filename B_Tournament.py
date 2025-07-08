T = int(input())

def solve():

    n,j,k = list(map(int,input().split()))
    nums = list(map(int,input().split()))

    if k>1:
        print("YES")
        return 
    if max(nums)==nums[j-1]:
        print("YES")
        return
    print("NO")
    return 

for _ in range(T):
    solve()
