import sys
input = sys.stdin.readline

def count_winning_triples(a):
    n = len(a)
    maxv = a[-1]
    total = 0

    # For each k in [2..n-1], count pairs (i<j<k) with a[i]+a[j] > T
    for k in range(2, n):
        T = max(a[k], maxv - a[k])
        l, r = 0, k-1
        # two-pointer on prefix a[0..k-1]
        while l < r:
            if a[l] + a[r] > T:
                total += (r - l)
                r -= 1
            else:
                l += 1

    return total

def main():
    t = int(input())
    out = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        # a is non-decreasing by problem guarantee
        out.append(str(count_winning_triples(a)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
