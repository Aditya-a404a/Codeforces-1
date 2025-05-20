n,m = list(map(int, input().split()))
s = input()
seen = set(input().split())

ans = 0 

c =0
p = 0 
while p<len(s):
    if s[p] in seen:
        c+=1
        ans+=c
    else:
        c=0
    p+=1
print(ans)
