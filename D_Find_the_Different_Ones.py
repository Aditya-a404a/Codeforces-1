T = int(input())


def solve():

    n = int(input())
    A = list(map(int, input().split()))

    p = [-1]*(n)

    for i in range(1,n):
        p[i] = p[i-1]
        if A[i]!=A[i-1]:
            p[i] = i-1
    m = int(input())
    for i in range(m):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        if p[r] <l:
            print("-1 -1")
        else:
            print(p[r]+1, r+1)

    





for _ in range(T):
    solve()