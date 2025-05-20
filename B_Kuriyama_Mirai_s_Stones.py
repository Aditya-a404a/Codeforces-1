n = int(input())

A = list(map(int, input().split()))
T = A.copy()
T.sort()
a = [0]*(len(A)+1)
b = [0]*(len(A)+1)

for i in range(1,len(A)+1):
    a[i] = a[i-1]+A[i-1]
    b[i] = b[i-1]+T[i-1]


m = int(input())
for _ in range(m):
    ty, l, r = map(int, input().split())
    if ty==1:
        print(a[r]-a[l-1])
    else:
        print(b[r]-b[l-1])