T = int(input())

def check(a,b):

    a = [ (min(x,y),max(x,y)) for x,y in zip(a,b)]

    #    1      2     0 
    # (0,0),(0,1),(1,1)
    flg = 0
    flg2 = 0  
    ans = 0 
    # print(a)
    for x  in a :
        if x==("1","1"):
            if flg :
                ans+=1
                flg = flg2 = 0   
            else:
                flg2 = 1 
        if x==("0","1"):
            ans+=2
            flg = flg2 = 0
            
        if x==("0","0"):
            if flg2:
                ans+=2
                flg = flg2 = 0
            else:
                ans+=1
                flg = 1   
    return ans


    


        
        






for _ in range(T):
    n = int(input())
    a  = input()
    b =  input()

    print(check(a, b))