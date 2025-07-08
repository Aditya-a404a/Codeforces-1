import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        p = [0] * n
        p[0] = a[0]
        for i in range(1, n):
            p[i] = min(p[i-1], a[i])
        S = [0] * n
        S[0] = p[0]
        for i in range(1, n):
            S[i] = S[i-1] + p[i]
        best = S[n-1]
        best0 = 10**30
        for j in range(1, n):
            best0 = min(best0, S[j-1] + a[j])
        if best0 < best:
            best = best0
        can = [False] * n
        for i in range(1, n):
            can[i] = a[i] >= p[i-1]
        any_safe = False
        for j in range(2, n):
            any_safe |= can[j-1]
            if any_safe and S[j-1] < best:
                best = S[j-1]
        print(best)

if __name__ == "__main__":
    solve()
