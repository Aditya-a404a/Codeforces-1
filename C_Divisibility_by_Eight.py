def solve():
    s = list(map(int,list(input())))
    n = len(s)

    dp =  [[False]*8 for x in range(n+1)] 
    prev = [[False]*8 for x in range(n+1)]

    for x in range(1,n+1):

        d = s[x-1]
        mod = d%8
        dp[x][mod] = True
        prev[x][mod]=(-1,d)

        for y in range(8):

            if dp[x-1][y]==True:

                dp[x][y] = True
                if not prev[x][y]:
                    prev[x][y]=(y,None)
                nw = (y*10+d)%8
                dp[x][nw] = True
                prev[x][nw]=(y,d)

    for i in range(1,len(dp)):
        if dp[i][0]:

            res = []
            mod = 0 
            while i > 0:
                prev_mod , digit = prev[i][mod]
                if digit!=None:
                    res.append(str(digit))
                if prev_mod==-1:
                    break
                mod = prev_mod
                i-=1
            print("YES")
            print("".join(res)[::-1])
            break
    else:
        print("NO")
solve()




