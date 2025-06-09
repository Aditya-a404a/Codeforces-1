T = int(input())

def solve(nums):

    a ,b,c,d = nums
    f = min(b,d)
    g = min(a,c)

    if g < f:
        print("Flower")
        return
    else:
        print("Gellyfish")
        return "Gellyfish"
    pass

for _ in range(T):

    arr = list(map(int,input().split()))
    solve(arr)