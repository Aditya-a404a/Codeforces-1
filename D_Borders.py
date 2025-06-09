def build_suffix_array(s):
    n = len(s)
    k = 1
    rank = [ord(c) for c in s]
    tmp = [0] * n
    sa = list(range(n))
    while True:
        sa.sort(key=lambda x: (rank[x], rank[x + k] if x + k < n else -1))
        tmp[sa[0]] = 0
        for i in range(1, n):
            tmp[sa[i]] = tmp[sa[i - 1]] + (
                (rank[sa[i]] != rank[sa[i - 1]]) or
                (rank[sa[i] + k] if sa[i] + k < n else -1) !=
                (rank[sa[i - 1] + k] if sa[i - 1] + k < n else -1)
            )
        rank = tmp[:]
        if rank[sa[-1]] == n - 1:
            break
        k <<= 1
    return sa

def build_lcp(s, sa):
    n = len(s)
    rank = [0] * n
    for i in range(n):
        rank[sa[i]] = i
    lcp = [0] * (n - 1)
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i] - 1] = h
            if h > 0:
                h -= 1
    return lcp

def prefix_function(t):
    n = len(t)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and t[i] != t[j]:
            j = pi[j - 1]
        if t[i] == t[j]:
            j += 1
        pi[i] = j
    return pi

def count_borders_from_pi(pi, length):
    # Count number of borders for prefix of length `length`
    count = 0
    while length > 0:
        length = pi[length - 1]
        if length > 0:
            count += 1
    return count

def total_borders(s):
    sa = build_suffix_array(s)
    lcp = build_lcp(s, sa)

    # Precompute prefix function for full string once
    pi = prefix_function(s)

    total = 0
    for l in lcp:
        total += count_borders_from_pi(pi, l)

    return total

# Input and Output
import sys
input = sys.stdin.readline
s = input().strip()
print(total_borders(s))
