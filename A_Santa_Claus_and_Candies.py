def distribute(n):
    # find the largest k such that 1+2+...+k <= n
    k = 0
    total = 0
    while total + (k+1) <= n:
        k += 1
        total += k

    # total = 1 + 2 + ... + k ≤ n
    # leftover candies
    r = n - total

    # base distribution: 1, 2, ..., k
    kids = list(range(1, k+1))

    # dump the remainder onto the last kid
    if r > 0:
        kids[-1] += r

    return kids

if __name__ == "__main__":
    n = int(input())
    kids = distribute(n)
    print(len(kids))
    print(*kids)
