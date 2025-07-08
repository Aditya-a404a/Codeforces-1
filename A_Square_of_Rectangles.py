t = int(input())

def solve():
    
    l,b,l1,b1,l2,b2 = list(map(int,input().split()))
    
    if l==l1==l2:
        if b1+b+b2==l:
            print("YES")
            return
    else:
        if l1+l2==l:
            if b1==b2:
                if b1+b==l:
                    print("YES")
                    return
    if b1==b==b2:
        if l1+l+l2==b:
            print("YES")
            return
    else:
        if b1+b2==b:
            if l1==l2:
                if l1+l==b:
                    print("YES")
                    return 
    print("NO")
    
for _ in range(t):
    solve()

