
s = input().strip()
s += '$'

# Counting sort using current equivalence classes
# Adjusted to size by number of classes and count only over p
def count_sort(p, c):
    n = len(p)
    num_classes = max(c) + 1
    count = [0] * num_classes
    for x in p:
        count[c[x]] += 1
    pos = [0] * num_classes
    for i in range(1, num_classes):
        pos[i] = pos[i-1] + count[i-1]
    p_new = [0] * n
    for x in p:
        cls = c[x]
        p_new[pos[cls]] = x
        pos[cls] += 1
    return p_new

# Build suffix array
n = len(s)
a = [(ch, i) for i, ch in enumerate(s)]
a.sort()
p = [idx for (_, idx) in a]
# Initial equivalence classes
c = [0] * n
for i in range(1, n):
    c[p[i]] = c[p[i-1]] + int(a[i][0] != a[i-1][0])

k = 0
while (1 << k) < n:
    shift = 1 << k  # properly parenthesized shift
    # Rotate p by -2^k
    p = [(pi - shift + n) % n for pi in p]
    # Stable sort by class
    p = count_sort(p, c)
    # Recompute classes
    c_new = [0] * n
    c_new[p[0]] = 0
    for i in range(1, n):
        prev, curr = p[i-1], p[i]
        pair_prev = (c[prev], c[(prev + shift) % n])
        pair_curr = (c[curr], c[(curr + shift) % n])
        c_new[curr] = c_new[prev] + int(pair_curr != pair_prev)
    c = c_new
    k += 1  # ensure k increments each iteration

# Remove sentinel suffix
p = p[1:]

qcount = int(input())
for _ in range(qcount):
    query = input().strip()
    left, right = 0, len(p) - 1
    found = False
    while left <= right:
        mid = (left + right) // 2
        start = p[mid]
        # Compare up to query length, handle short suffix
        if start + len(query) <= len(s):
            suffix_part = s[start:start + len(query)]
        else:
            suffix_part = s[start:]
        if suffix_part == query:
            print("Yes")
            found = True
            break
        elif suffix_part > query:
            right = mid - 1
        else:
            left = mid + 1
    if not found:
        print("No")


    




