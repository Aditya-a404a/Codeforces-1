T = int(input())


def check(A):
    n = len(A)
    A.sort()
    s = A[0]
    if A[0]!=1:
        return "NO"
    for x in range(1,len(A)):
        if A[x] > s:
            return "NO"
        s += A[x]
    return "YES"


    
    



    pass

for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    print(check(nums))
