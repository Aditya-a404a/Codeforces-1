import sys
input = sys.stdin.readline

def solve():
    n, k, x = map(int, input().split())
    B = list(map(int, input().split()))
    
    total = sum(B) * k
    if total < x:
        print(0)
        return

    # Build prefix-sum of one copy of B
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i+1] = pref[i] + B[i]

    left, right = 1, n * k
    while left <= right:
        mid = (left + right) // 2
        
        # Sum of the first `mid` elements of B repeated k times:
        full_blocks = mid // n
        rem = mid % n
        removed_sum = full_blocks * sum(B) + pref[rem]
        
        # Suffix sum = total sum – removed_sum
        if total - removed_sum < x:
            # mid is already too large a prefix (suffix sum too small),
            # so try a smaller mid
            right = mid - 1
        else:
            # suffix sum still ≥ x, need to remove more, so increase mid
            left = mid + 1

    # `left` is now the smallest ℓ such that suffix_sum < x
    print(left)

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        solve()
