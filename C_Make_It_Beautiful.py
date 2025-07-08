T = int(input())


def solve():

    n,k = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    ans = sum( x.bit_count() for x in nums )
    for x in range(61):
        target = 1<<x
        count = 0 
        for y in nums:
            if not (y&target):
                count+=1
        ans+=min(count,k//target)
        k-=count*target
        if k<1:
            print(ans)
            return 
    print(ans)
    return 
    pass


for x in range(T):
    solve()

