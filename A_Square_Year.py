T = int(input())


def solve(n):

    for x in range(0,100):
        for y in range(0,100):
            if x**2+y**2+2*x*y ==n:
                print(x,y)
                return 
    print(-1)
    return 


    pass

for _ in range(T):

    solve(int(input()))