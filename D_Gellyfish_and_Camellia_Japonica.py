T = int(input())
from collections import defaultdict
def solve():
    n , q = list(map(int,input().split()))
    B = list(map(int,input().split()))
    Q = []
    for x in range(q):
        Q.append(list(map(int,input().split())))
    A = [0]*n
    Q = Q[::-1]
    graph = defaultdict(list)
    for i,(x,y,z) in enumerate(Q):
        q.append((i,x-1,y-1,z-1))
    q.sort()
    A = [0]*n
    for i,x,y,z in enuemra
    print(graph.items())
    pass

for _ in range(T):

    solve();