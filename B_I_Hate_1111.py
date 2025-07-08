T = int(input())

def solve():

    n =  int(input())
    for x in range(11):
        t = n - 111*x
        if t>=0 and t%11==0:
            print("YES")
            return 
    print("NO")
    return 

for _ in range(T):

    solve()
