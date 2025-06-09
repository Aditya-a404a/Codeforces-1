

def solve():
    s = input()

    for x in range(len(s)-1):

        if s[x:x+2]=="AB":
            for y in range(x+2,len(s)-1):
                if s[y:y+2]=="BA":
                    return "YES"
            break
    for x in range(len(s)-1):

        if s[x:x+2]=="BA":
            for y in range(x+2,len(s)-1):
                if s[y:y+2]=="AB":
                    return "YES"
            break
    return "NO"
    
print(solve())
                




