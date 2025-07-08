from bisect import bisect_right
from collections import defaultdict

def solve():
    n, s, mx = map(int, input().split())
    nums = list(map(int, input().split()))

    # map from prefix‐sum → sorted list of prefix‐indices
    dic = defaultdict(list)
    dic[0].append(0)

    p = 0
    count = 0

    last_bad_pos = -1    # last i with nums[i] > mx
    last_mx_pos  = -1    # last i with nums[i] == mx

    for x, v in enumerate(nums):
        p += v
        if v > mx:
            last_bad_pos = x
        if v == mx:
            last_mx_pos = x

        # look for f so that p - p[f] == s ⇒ p[f] == p - s
        target = p - s
        if target in dic and last_mx_pos > last_bad_pos:
            flist = dic[target]
            # count how many f satisfy: last_bad_pos < f ≤ last_mx_pos
            L = bisect_right(flist, last_bad_pos)
            R = bisect_right(flist, last_mx_pos)
            count += (R - L)

        # record this prefix index (x+1) in sorted order
        dic[p].append(x+1)

    print(count)

T = int(input())
for _ in range(T):
    solve()

