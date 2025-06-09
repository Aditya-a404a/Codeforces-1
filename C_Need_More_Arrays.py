T = int(input())


def solve(arr):

    prev = -1
    count = 0
    for x in arr:
        if prev+1<x:
            count+=1
            prev=x
    print(count)        
    return



    pass


for _ in range(T):
    n = int(input())

    arr = list(map(int,input().split()))
    solve(arr)
