n,q = list(map(int,input().split()))

p = [0]*(n+2)
nums = list(map(int,input().split()))
for _ in range(q):
    l,r = list(map(int,input().split()))
    p[l]+=1
    p[r+1]-=1
for x in range(1,len(p)):
    p[x]+=p[x-1]
p.sort()
nums.sort()
count = 0 
while nums:
    count+=nums.pop()*p.pop()
print(count)





