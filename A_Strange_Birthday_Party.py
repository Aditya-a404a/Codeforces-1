T = int(input())

def check(A,B):
    A.sort()
    cost = 0 
    i = 0 
    while A:
        k = A.pop()
        if i<len(B) and i<=k:
            cost+=min(B[i],B[k-1])
            i+=1
        else:
            cost+=B[k-1]
    return cost


    pass
for _ in range(T):
    n,m = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B =  list(map(int,input().split()))
    print(check(A,B))





