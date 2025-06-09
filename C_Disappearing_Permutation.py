T = int(input())


def solve():
    
    n = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A = [x-1 for x in A]
    B = [x-1 for x in B]

    seen = set()
    res = [ ]
    for x in B:
        while x not in seen:
            seen.add(x)
            x = A[x]
        res.append(len(seen))
    print(*res)
    return 
for _ in range(T):
    solve()

