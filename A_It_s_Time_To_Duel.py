T =  int(input())


def solve():
    n = int(input())
    A = list(map(int,input().split()))
    if A==[1]*n:
        print("YES")
        return 
    if A==[0]*n:
        print("YES")
        return
    print("NO")
    return

    pass


for _ in range(T):
    solve()