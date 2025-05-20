T = int(input())

def check(A):
    mx = A[0]
    s = 0 
    
    for x in range(1,len(A)):
        if A[x-1]//abs(A[x-1]) != A[x]//abs(A[x]):
            s += mx
            mx = A[x]
        else:
            mx = max(mx, A[x])
    return s + mx
    






    pass

for _ in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    print(check(A))
