T = int(input())
from collections import defaultdict
def solve():
    n = int(input())
    s = input()
    dic = defaultdict(int)
    for i,x in enumerate(s):
        dic[x]+=1
        if dic[x]>=2 and i!=len(s)-1:
            print("Yes")
            return
    dic = defaultdict(int)
    for i,x in enumerate(s[::-1]):
        dic[x]+=1
        if dic[x]>=2 and i!=len(s)-1:
            print("Yes")
            return
    print("No")
    return 
    



for _ in range(T):
    solve()
