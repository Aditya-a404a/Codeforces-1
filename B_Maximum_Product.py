#!/usr/bin/env python3
import sys
import math

def max_product_of_five(a):
    n = len(a)
    # Find the maximum element to check if all are negative
    mx = max(a)
    # Sort descending by absolute value
    a.sort(key=abs, reverse=True)

    # If all elements are negative, pick the five with smallest abs (to get the largest negative product)
    if mx < 0:
        a.sort(key=abs)
        return math.prod(a[:5])

    # Otherwise, start with the product of the top 5 by abs
    ans = math.prod(a[:5])

    # Try replacing each of the first 5 picks with each later element
    # (mirrors the double loop in your C++ code)
    for i in range(5, n):
        for j in range(5):
            tmp = a[i]
            for k in range(5):
                if k != j:
                    tmp *= a[k]
            ans = max(ans, tmp)

    return ans

def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(max_product_of_five(arr))

if __name__ == "__main__":
    main()
