import sys
input = sys.stdin.readline

def solve():
    n, q = map(int, input().split())
    s1 = input().strip()
    s2 = input().strip()

    # Build prefix‐sum arrays for both strings
    # pre1[i][c] = count of chr(c+'a') in s1[:i]
    pre1 = [[0]*26 for _ in range(n+1)]
    pre2 = [[0]*26 for _ in range(n+1)]

    for i, ch in enumerate(s1, start=1):
        idx = ord(ch) - ord('a')
        # copy previous counts
        row = pre1[i]
        prev = pre1[i-1]
        for c in range(26):
            row[c] = prev[c]
        # increment this character
        row[idx] += 1

    for i, ch in enumerate(s2, start=1):
        idx = ord(ch) - ord('a')
        row = pre2[i]
        prev = pre2[i-1]
        for c in range(26):
            row[c] = prev[c]
        row[idx] += 1

    # Answer queries
    out = []
    for _ in range(q):
        l, r = map(int, input().split())
        diff = 0
        # for each letter, compute abs difference in [l..r]
        for c in range(26):
            v1 = pre1[r][c] - pre1[l-1][c]
            v2 = pre2[r][c] - pre2[l-1][c]
            diff += abs(v1 - v2)
        # Each swap fixes two mismatches
        out.append(str(diff // 2))

    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        solve()
