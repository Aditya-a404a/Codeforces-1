def solve():
    s = [int(x) for x in list(input())]

    sm = sum(s)
    twos = s.count(2)
    threes = s.count(3)

    for i in range(min(10, twos + 1)):
        for j in range(min(10, threes + 1)):
            if (sm + i * 2 + j * 6) % 9 == 0:
                print('YES')
                return
    print('NO')


t = int(input())
for _ in range(t):
    solve()