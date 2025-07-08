def solve():
    n, k = map(int, input().split())
    s = input().strip()
    
    ones = s.count('1')
    
    if ones <= k:
        return "Alice"
    
    
    prefix_ones = s[:k].count('1')
    suffix_ones = s[n-k:].count('1') if k < n else 0

    if 2 * k >= n:
        return "Alice"
    
    
    if ones < prefix_ones + suffix_ones:
        return "Alice"
    else:
        return "Bob"

t = int(input())
for _ in range(t):
    print(solve())