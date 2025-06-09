import sys
input = sys.stdin.read
sys.setrecursionlimit(1 << 25)

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
                (rank[sa[i] + k] if sa[i] + k < n else -1) != (rank[sa[i - 1] + k] if sa[i - 1] + k < n else -1)
            )
        rank = tmp[:]
        if rank[sa[-1]] == n - 1:
            break
        k <<= 1
    return sa, rank

def compare_substrings(s, a, b):
    l1, r1 = a
    l2, r2 = b
    len1 = r1 - l1 + 1
    len2 = r2 - l2 + 1
    min_len = min(len1, len2)
    for i in range(min_len):
        if s[l1 + i] != s[l2 + i]:
            return s[l1 + i] < s[l2 + i]
    if len1 != len2:
        return len1 < len2
    if l1 != l2:
        return l1 < l2
    return r1 < r2

def main():
    data = input().split()
    s = data[0]
    n = int(data[1])
    queries = [(int(data[i]) - 1, int(data[i + 1]) - 1) for i in range(2, 2 + 2 * n, 2)]

    build_suffix_array(s)  # we don't need it for this logic but kept for completeness

    queries.sort(key=lambda x: (
        s[x[0]:x[1] + 1],  # Pythonic lexicographical substring sort (not optimal but works)
        x[0], x[1]
    ))

    for l, r in queries:
        print(l + 1, r + 1)

if __name__ == "__main__":
    main()

