T = int(input())


def check(A):

    even = []
    odd = []
    A.sort()
    for x in A:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    a = 0
    b = 0
    chance = 0
    while  chance!=len(A):
        if chance%2==0:
            if len(odd)==0:
                o=0 
            else:
                o = odd.pop()
            if len(even)==0:
                e = 0 
            else:
                e = even.pop()
            if e > o:
                a+=e
                odd.append(o)
            else:
                even.append(e)
        else:
            if len(odd)==0:
                o=0 
            else:
                o = odd.pop()
            if len(even)==0:
                e = 0 
            else:
                e = even.pop()
            if e < o:
                b+=o
                even.append(e)
            else:
                odd.append(o)
        chance+=1
    if a > b:
        return "Alice"
    elif a < b:
        return "Bob"
    return "Tie"
    pass

for _ in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    print(check(A))