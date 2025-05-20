T = int(input())

def solve(n,x):
    s = bin(x)[2:]
    c = 0 
    for t in s:
        c+= int(t)
    if n<=c:
        return x;
    if (n-c)%2==0:
        return x+n-c
    else:
        if x > 1 :
            return x+n-c+1
        if x==1:
            return n+3
        else:
            if (n==1):
                return -1
            return n+3


for _ in range(T):
    n , x = map(int, input().split())
    print(solve(int(n),int(x)))
    