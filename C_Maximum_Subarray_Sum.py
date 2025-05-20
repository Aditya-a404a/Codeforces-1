T = int(input())
inf = 10**13


def solve(n,k,arr,s):

    ans = 0 
    curr = 0
    pos = -1 
    for i,x in enumerate(s):

        if x=="0":
            pos = i
            arr[i] = -inf
    for x in arr:
        if curr < 0:
            curr =0 
        curr +=x
        ans = max(ans, curr)
    
    if ans > k :
        print("No")
        return []
    if ans == k:
        print("Yes")
        return arr
    if pos !=-1 :
        arr[pos] = 0
        curr = 0 
        mx = 0 
        for x in range(pos+1,len(arr)):
            curr+=arr[x]
            mx = max(mx, curr)
        L = mx
        curr = 0 
        mx = 0 
        for x in range(pos-1,-1,-1):
            curr+=arr[x]
            mx = max(mx, curr)
        R = mx
        arr[pos] = k - L - R
        print("Yes")
        return arr
    print("No")
    return []
    




    
    



for _ in range(T):
    n, k = map(int,input().split())
    s = input()
    arr = list(map(int, input().split()))
    ans = solve(n,k,arr,s)
    if len(ans)!=0:
        print(*ans)
    
