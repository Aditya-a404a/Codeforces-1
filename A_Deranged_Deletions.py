T = int(input())

def solve():

    n = int(input())
    nums = list(map(int,input().split()))

    if n==1:
        print("NO")
        return
    for x in range(n):
        for y in range(x+1,n):
            if nums[x] > nums[y]:
                print("YES")
                print(2)
                print(nums[x],nums[y])
                return
    print("NO")
    return 
for _ in range(T):
    solve()
    
