s = input()

s+="$"

def count_sort(p,c):
    n = len(p)
    count = [0]*n

    for x in c:
        count[x]+=1
    
    pos = [0]*n
    for x in range(1,len(p)):
        pos[x] = pos[x-1] + count[x-1]
    newp = [0]*n
    for x in p:
        i = c[x]
        newp[pos[i]]=x
        pos[i]+=1
    return newp

n = len(s)

a = [ (x,i) for i,x in enumerate(s)]
a.sort()
p = [x[-1] for x in a]
c = [0]*n
for x in range(1,n):
    c[p[x]]=c[p[x-1]]+int(a[x][0]!=a[x-1][0])
k = 0 

while (1<<k) < n:

    p = [ (x - (1<<k) + n )%n for x in p ]
    p = count_sort(p,c)

    newc = [0]*n
    for x in range(1,n):

        now = ( c[p[x]] , c[ (p[x]+(1<<k))%n ])
        prev = ( c[p[x-1]] , c[ (p[x-1]+(1<<k))%n ])

        newc[p[x]] = newc[p[x-1]]+int(now!=prev)
    k+=1
    c = newc

lcp = [0]*n
k =0 
for i in range(n-1):
    pi = c[i]
    j = p[pi-1]

    while s[i+k]==s[j+k]:
        k+=1
    lcp[pi] = k 
    k = max(k-1,0)
print(*p)
print(*lcp[1:])


