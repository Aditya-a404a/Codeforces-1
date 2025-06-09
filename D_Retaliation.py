import sys
input = sys.stdin.readline

def can_explode(n, a):
    S = n * (n + 1) // 2
    if sum(a) % S:
        return False
    k = sum(a) // S
    d = a[1] - a[0]
    if (k + d) & 1:
        return False
    x = (k + d) // 2
    y = k - x
    if x < 0 or y < 0:
        return False
    for i, v in enumerate(a, 1):
        if v != x * i + y * (n - i + 1):
            return False
    return True

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print("YES" if can_explode(n, a) else "NO")

solve()