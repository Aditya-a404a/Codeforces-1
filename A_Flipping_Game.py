n = input()

B = list(map(int, input().split()))
def check(A):
    if [1]*len(A)==A:
        return len(A)-1
    a = [0]*len(A)
    ans = 0 
    for i in range(len(A)):
        ans+=A[i]
        if A[i] == 1:
            a[i] = -1
        else:
            a[i] = 1
    
    curr = 0
    mx = 0
    for x in a:
        curr+=x
        if curr<0:
            curr = 0
        mx = max(mx, curr)
    return ans+mx
    pass

print(check(B))