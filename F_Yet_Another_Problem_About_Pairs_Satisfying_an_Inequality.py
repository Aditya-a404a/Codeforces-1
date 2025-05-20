import sys
import bisect

def solve():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        res = 0
        v = []  # will store previous indices j (1-based) where a[j] < j
        
        for i, ai in enumerate(a, start=1):  # i is 1-based
            if ai < i:
                # count how many j in v satisfy j < ai
                # since v is always sorted (we only append increasing i),
                # bisect_left(v, ai) gives number of j < ai
                cnt = bisect.bisect_left(v, ai)
                res += cnt
                # record this index for future i's
                v.append(i)
                
        print(res)

if __name__ == "__main__":
    solve()
