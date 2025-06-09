s1 = input().strip()
s2 =""

# build the concatenated string with unique sentinels

def count_sort(p,c):
    n = len(p)
    count = [0]*n
    for x in c:
        count[x]+=1
    pos = [0]*n
    for x in range(1,n):
        pos[x] = pos[x-1]+count[x-1]
    newp = [0]*n
    for x in p:
        i = c[x]
        newp[pos[i]]=x
        pos[i]+=1
    return newp

sep1, sep2 = '$', ''
s = s1 + sep1 + s2 + sep2
n = len(s)
f = len(s1)

a = [(x,i) for i,x in enumerate(s)]
a.sort()
p = [ x[1] for x in a]

c = [0]*n
for x in range(1,n):

    c[p[x]] = c[p[x-1]]+int(a[x][0]!=a[x-1][0])

k = 0 
while ( 1<< k ) < n:
    
    p = [ ( x - (1<<k)+ n)%n for x in p]
    p = count_sort(p,c)
    newc = [0]*n
    for x in range(1,n):

        curr = ( c[p[x]],c[(p[x]+1<<k)%n])
        prev = ( c[p[x-1]],c[(p[x-1]+1<<k)%n])
        newc[p[x]] = newc[p[x-1]] + int(curr!=prev)

    c = newc
    k+=1
print(p)
print(c)