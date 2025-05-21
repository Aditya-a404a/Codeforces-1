def count_beautiful_substrings(s: str) -> int:

    n = len(s)
    ans = 0 
    a = -1
    b = -1 
    for x in range(len(s)):

        c = s[x]

        ea = (x%2)^0 
        eb = (x%2)^1
        if c!="?" and ea!=int(c):
            a = x
        if c!="?" and eb!=int(c):
            b = x
        mi = min(a,b)
        ans+=x-mi
    return ans 

    

# Reading input and running
t = int(input())
for _ in range(t):
    s = input().strip()
    print(count_beautiful_substrings(s))


