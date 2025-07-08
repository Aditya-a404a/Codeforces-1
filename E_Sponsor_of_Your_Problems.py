import sys
from functools import lru_cache

def solve():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        l, r = input().split()
        n = len(l)
        L = list(map(int, l))
        R = list(map(int, r))

        @lru_cache(None)
        def dfs(i, gl, lr):
            if i == n:
                return 0

            lo = L[i] if gl == 0 else 0
            hi = R[i] if lr == 0 else 9

            best = 10**9
            for d in range(lo, hi + 1):
                # new flags
                ngl = gl or (d > L[i])
                nlr = lr or (d < R[i])
                cost = (d == L[i]) + (d == R[i])
                val = cost + dfs(i + 1, ngl, nlr)
                if val < best:
                    best = val
            return best

        
        ans = dfs(0, 0, 0)
        print(ans)

if __name__ == "__main__":
    solve()
