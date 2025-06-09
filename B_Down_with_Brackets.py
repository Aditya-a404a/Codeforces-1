T = int(input())


def solve(s):

    # op = len(s)-1
    # while op >=0 and s[op]=="(":
    #     op-=1
    # cl = 0 
    # while cl <len(s) and s[cl]==")":
    #     cl+=1
    s = s[1:len(s)-1]
    
    bal =  0
    for x in range(len(s)):
        
        # if x==cl:
        #     continue
        # if x==op:
        #     continue
        bal+=int(s[x]=="(")
        bal-=int(s[x]==")")
        if bal < 0 :
            return "YES"
    return "NO"
    pass


for _ in range(T):

    s = input()
    print(solve(s))