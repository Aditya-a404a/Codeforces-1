
import math 
import sys
import math

input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        # Precompute prefix- and suffix-GCDs so we can get
        # gcd of everything except a[i] in O(1).
        pref = [0] * (n+1)
        suf  = [0] * (n+1)
        for i in range(n):
            pref[i+1] = math.gcd(pref[i], a[i])
        for i in range(n-1, -1, -1):
            suf[i] = math.gcd(suf[i+1], a[i])

        found = False
        ans = [2] * n  # default: put everything in C (label 2)
        for i in range(n):
            g_rem = math.gcd(pref[i], suf[i+1])
            if g_rem != a[i]:
                # put a[i] in B (label 1), rest in C (2)
                ans[i] = 1
                print("Yes")
                print(*ans)
                found = True
                break

        if not found:
            print("No")
solve()
    
