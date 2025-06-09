T = int(input())
from collections import defaultdict

def solve():

    n , m = list(map(int,input().split()))
    s = input()
    op = [ ]
    for x in range(m):
        op.append(input().split())

    indexs = defaultdict(list)
    for x in range(len(s)):
        if s[x]=="b":
            indexs[s[x]].append(x)
        elif s[x]=="c":
            indexs[s[x]].append(x)
    indexs["b"] = indexs["b"][::-1]
    indexs["c"] = indexs["c"][::-1]
    print("b",indexs["b"])
    print("c",indexs["c"])
    print(s)
for _ in range(T):
    solve()

