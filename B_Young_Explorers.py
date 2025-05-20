T = int(input())


def check(A):
    A.sort() 
    ans  =  0 
    mx = A[0]
    curr = 1
    for i in range(1,len(A)):
        
        if  mx <=curr:
            
            ans += 1
            curr = 1
            mx = A[i]
        else:
            mx = max(mx,A[i])
            curr += 1
    return ans+int(mx<=curr)

    pass

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(check(A))

    
