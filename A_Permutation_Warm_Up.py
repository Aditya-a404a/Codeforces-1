T = int(input())


def solve(n):
    return (n**2)//4 + 1
    pass

for _ in range(T):

    n = int(input())
    print(solve(n))
