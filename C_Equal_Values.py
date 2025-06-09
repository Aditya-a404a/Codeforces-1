T = int(input())


def solve():

    n = int(input())
    A = list(map(int,input().split()))

    best = float('inf')
    prev = -1
    c = 0 
    for x in range(n):

        if prev!=A[x]:
            c=1
            prev = A[x]
        else:
            c+=1
        best = min(best,(n-c)*A[x])
    print(best)
    return 0
for _ in range(T):
    solve()