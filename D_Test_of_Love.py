def solve():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        s = input()
        dp = [-1] * (n + 2)
        dp[0] = k

        for i in range(1, n + 2):
            if i != n + 1 and s[i - 1] == 'C':
                continue
            for t_ in range(1, m + 1):
                if i - t_ >= 0 and (i - t_ == 0 or s[i - t_ - 1] == 'L'):
                    dp[i] = max(dp[i], dp[i - t_])
            if i > 1 and s[i - 2] == 'W':
                if dp[i - 1] > -1:
                    dp[i] = max(dp[i], dp[i - 1] - 1)

        print("YES" if dp[n + 1] >= 0 else "NO")

solve()
