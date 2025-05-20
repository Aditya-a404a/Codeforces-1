import sys
input = sys.stdin.readline

MAX = 200_007
res = [0] * MAX

def digit_sum(x):
    s = 0
    while x:
        s += x % 10
        x //= 10
    return s

# Precompute: res[i] = res[i-1] + sum_of_digits(i)
for i in range(1, MAX):
    res[i] = res[i-1] + digit_sum(i)

def main():
    t = int(input())
    for _ in range(t):
        x = int(input())
        # direct lookup
        print(res[x])

if __name__ == "__main__":
    main()
