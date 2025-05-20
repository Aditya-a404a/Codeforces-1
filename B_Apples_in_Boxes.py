T = int(input())


def solve(n,k,arr):
    arr.sort()

    s = sum(arr) 
    arr[-1]-=1
    arr.sort()
    if arr[-1] - arr[0] > k or s%2==0:
        return "Jerry"
    else:
        return "Tom"
    
    



for _ in range(T):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(n,k,arr))
