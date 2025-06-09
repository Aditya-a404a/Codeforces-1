T = int(input())

def solve(arr, k):
    arr = [ (x%k,x) for x in arr]
    left = 0
    right = len(arr)-1
    count =0
    print(arr)
    while left<=right:
        if left==right:
            break
        if arr[left][0]!=arr[right][0]:
            print(count)
            return -1
        else:
            count+=abs(arr[left][1]-arr[right][1])//k
            left+=1
            right-=1
    print(count)
    return count

    pass


for _ in range(T):

    k  = int(input())
    D = list(map(int,input().split()))
    
    solve(D,k)
