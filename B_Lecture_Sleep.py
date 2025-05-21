n , k = list(map(int,input().split()))

A = list(map(int,input().split()))
T = list(map(int,input().split()))

s = 0 

for x,y in zip(A,T):
    if y==1:
        s+=x
l = 0
mx = s 
for x in range(len(A)):
    if T[x]==0:
        s+=A[x]
    if x>=k:
        if T[x-k]==0:
            s-=A[x-k]
    if x>=k-1:
        mx = max(mx,s)
print(mx)
        
