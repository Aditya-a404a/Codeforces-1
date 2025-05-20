T = int(input())


def check(n, m, k):

    grid = [[0 for j in range(m)] for i in range(n)]
    
    
    return grid


   


for _ in range(T):

    n,m,k = list(map(int,input().split()))
    
    d = check(n,m,k)
    for x in range(n):
        for y in range(m):
            print(d[x][y],end=" ")
        print()

            