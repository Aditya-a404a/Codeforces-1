T = int(input())
inf = (2**33)
def check(A,B):
    prev = -inf

    choose = [ (min(x,B-x),max(x,B-x)) for x in A ]

    ans = [ ]
    for x in choose:
        if x[0] >= prev:
            ans.append(x[0])
            prev = x[0]
        elif x[1] >= prev:
            ans.append(x[1])
            prev = x[1]
        else:
            return "NO"
    return "YES"
   
    



for _ in range(T):
    input()
    a = list(map(int,input().split()))
    b = int(input())



    print(check(a,b))
