T = int(input())

def check(p,s):
    a = 0 
    b = 0 

    while a<len(p) and b<len(s):
        
        if p[a] == s[b]:
            i = a
            j = b
            count = 0
            while i < len(p) and p[i] == p[a] :
                count+=1
                i+=1
            while j < len(s) and s[j] == s[b] :
                j+=1
            if not ( count<=j-b<=count*2):
                return "NO" 
            a = i
            b = j
        else:
            return "NO"
    
    return "YES" if a == len(p) and b == len(s) else "NO"
for _ in range(T):

    print(check(input(),input()))