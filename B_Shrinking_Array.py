import sys
input = sys.stdin.readline
from collections import defaultdict

def solve():
    t = int(input())
    for _ in range(t):
        int(input())
        a = list(map(int, input().split()))

        last_pos = defaultdict(int)
        
        ans = float("inf")
        for i, v in enumerate(a):
            for w in (v-1, v, v+1):
                if w in last_pos:
                    
                    ops = i - last_pos[w] - 1
                    if ops < ans:
                        ans = ops
            last_pos[v] = i
        print(ans if ans < float("inf") else -1)

solve()



