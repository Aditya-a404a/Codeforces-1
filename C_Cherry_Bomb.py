def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    s = -1
    for i in range(n):
        if b[i] != -1:
            if s == -1:
                s = a[i] + b[i]
            elif s != a[i] + b[i]:
                print(0)
                return

    if s == -1:
        a.sort()
        mx = a[-1] - a[0]
        print(k - mx + 1)
        return

    for i in range(n):
        if a[i] > s or s - a[i] > k:
            print(0)
            return

    print(1)

t = int(input())
for _ in range(t):
    solve()
