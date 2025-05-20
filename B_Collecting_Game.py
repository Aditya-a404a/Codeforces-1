import sys
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        
        # Pair each value with its original index (0-based)
        pairs = [(arr[i], i) for i in range(n)]
        # Sort by value
        pairs.sort(key=lambda x: x[0])
        
        nxt = [0] * (n + 1)
        prefix_sum = [0] * (n + 1)
        ans = [0] * n
        
        # nxt[0] = 0, prefix_sum[0] = 0 by initialization
        
        for i in range(1, n + 1):
            val, orig_idx = pairs[i-1]
            
            # If previous block already reached at least i, reuse it
            if nxt[i-1] >= i:
                nxt[i] = nxt[i-1]
                prefix_sum[i] = prefix_sum[i-1]
            else:
                # Start a new block at i
                prefix_sum[i] = prefix_sum[i-1] + val
                nxt[i] = i
                # Expand as far as the running sum allows
                while nxt[i] < n and prefix_sum[i] >= pairs[nxt[i]][0]:
                    prefix_sum[i] += pairs[nxt[i]][0]
                    nxt[i] += 1
            
            # Store answer for this element’s original position
            # subtract 1 because we don’t count the initial removal
            ans[orig_idx] = nxt[i] - 1
        
        # Print answers in original order
        print(*ans)

if __name__ == "__main__":
    solve()
