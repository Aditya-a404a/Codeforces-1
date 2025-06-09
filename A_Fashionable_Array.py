T = int(input())

def solve(A):

    ans = 2**32
    A.sort()
    for x in range(len(A)):
        for y in range(len(A)):
            if (A[x]+A[y])%2==0:
                ans = min(ans,x+len(A)-y-1)
    return ans
    pass

for _ in range(T):
    n = int(input())
    A = list(map(int,input().split()))
    print(solve(A))




