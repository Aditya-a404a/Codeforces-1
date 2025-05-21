n = int(input())
from collections import defaultdict
A = list(map(int,input().split()))


dic = defaultdict(int)

A = [ (x-i) for i,x in enumerate(A)]

for i,x in enumerate(A):
    dic[x]+=(x+i)

print(max(dic.values()))



