import sys
input = sys.stdin.readline
MOD = 998244353

def solve():
    t = int(input())
    tests = []
    max_n = 0
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        q = list(map(int, input().split()))
        tests.append((n, p, q))
        max_n = max(max_n, n)
    # Precompute powers of two up to max_n
    pow2 = [1] * (max_n + 2)
    for i in range(1, max_n+2):
        pow2[i] = (pow2[i-1] * 2) % MOD

    out = []
    for n, p, q in tests:
        inv_p = [0]*n
        inv_q = [0]*n
        for idx, x in enumerate(p):
            inv_p[x] = idx
        for idx, x in enumerate(q):
            inv_q[x] = idx

        p_max = -1
        q_max = -1
        r = [0]*n

        for i in range(n):
            # update prefix maxima
            if p[i] > p_max:
                p_max = p[i]
            if q[i] > q_max:
                q_max = q[i]

            if p_max > q_max:
                M = p_max
                j0 = inv_p[M]
                S = q[i - j0]
            elif q_max > p_max:
                M = q_max
                k0 = inv_q[M]
                S = p[i - k0]
            else:
                # equal
                M = p_max  # == q_max
                # candidate 1: pair p-side
                j0 = inv_p[M]
                S1 = q[i - j0]
                # candidate 2: pair q-side
                k0 = inv_q[M]
                S2 = p[i - k0]
                S = S1 if S1 > S2 else S2

            # compute result modulo
            r[i] = (pow2[M] + pow2[S]) % MOD

        out.append(" ".join(map(str, r)))

    print("\n".join(out))


if __name__ == "__main__":
    solve()
