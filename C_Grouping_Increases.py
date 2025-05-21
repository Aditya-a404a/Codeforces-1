import sys
input = sys.stdin.read

INF = int(1e9 + 5)
data = input().split()
idx = 0

t = int(data[idx])
idx += 1

for _ in range(t):
    n = int(data[idx])
    idx += 1
    a = list(map(int, data[idx:idx + n]))
    idx += n

    t1 = INF
    t2 = INF
    ans = 0

    for num in a:
        if t1 > t2:
            t1, t2 = t2, t1
        if num <= t1:
            t1 = num
        elif num <= t2:
            t2 = num
        else:
            t1 = num
            ans += 1

    print(ans)
