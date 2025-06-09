T = int(input())
def solve():
    n = int(input())
    ans = 0 

    arr = [0,0,0]
    while arr!=[n]*3:
        ans+=1
        arr.sort()
        arr[0] = min(arr[1]*2+1,n)
        
    print(ans)
    return ans 



    pass

for _ in range(T):
    solve()
