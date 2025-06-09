T = int(input())


def solve():

    n,k = list(map(int,input().split()))
    s = input()
    count = [0]*2
    for x in s:
        count[int(x)]+=1
    need = k*2
    
    while  need>0 and count!=[0]*2:

        if count[0] < count[1]:
            count[0],count[1] = count[1],count[0]
        if count[0]-2>=0:
            need-=2
            count[0]-=2
        else:
            print("NO")
            return
    
    if count[0]==count[1]:
        print("YES")
        return 
    print("NO")
    return



for _ in range(T):
    

    solve()
