s = input()
s += "$"

def count_sort(p, c):
    n = len(p)
    count = [0] * n
    for x in c:
        count[x] += 1
    pos = [0] * n
    for x in range(1, n):
        pos[x] = pos[x - 1] + count[x - 1]
    
    newp = [0] * n
    for x in p:
        i = c[x]
        newp[pos[i]] = x
        pos[i] += 1
    return newp

n = len(s)

# Initial sorting by first character
a = sorted((char, i) for i, char in enumerate(s))
p = [x[1] for x in a]
c = [0] * n
for x in range(1, n):
    c[p[x]] = c[p[x - 1]] + (a[x][0] != a[x - 1][0])

k = 0
while (1 << k) < n:
    # Shift all positions by 2^k to prepare for sorting by 2k-length prefixes
    p = [(x - (1 << k) + n) % n for x in p]
    p = count_sort(p, c)

    c_new = [0] * n
    for x in range(1, n):
        curr = (c[p[x]], c[(p[x] + (1 << k)) % n])
        prev = (c[p[x - 1]], c[(p[x - 1] + (1 << k)) % n])
        c_new[p[x]] = c_new[p[x - 1]] + (curr != prev)
    c = c_new
    k += 1

# Kasai's Algorithm for LCP
lcp = [0] * n
k = 0
for x in range(n - 1):
    pi = c[x]
    if pi == 0:
        continue
    j = p[pi - 1]
    while x + k < n and j + k < n and s[x + k] == s[j + k]:
        k += 1
    lcp[pi] = k
    k = max(k - 1, 0)

# Counting distinct substrings
total = 0
for i in range(n):
    suffix_len = n - 1 - p[i]  # exclude '$'
    total += suffix_len - lcp[i]

print(total)




    