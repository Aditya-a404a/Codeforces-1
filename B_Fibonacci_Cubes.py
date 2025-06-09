T = int(input())


def solve():

    n , m = list(map(int,input().split()))
    fib = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    s =""
    for i in range(m):
        x,y,z = list(map(int,input().split()))

        mi = min(x,y,z)
        if mi < fib[n] : 
            s+='0'
            continue
        if fib[n]+fib[n-1]<=max(x,y,z):
            s+="1"
            continue 
        else:
            s+="0"
    print(s)
    return 0;

        
    pass



for _ in range(T):
    solve()

