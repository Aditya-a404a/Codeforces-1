from collections import defaultdict


T = int(input())

def check(A):
    n = len(A)

    mea = sum(A)/n
    target = mea*2
    dic = defaultdict(int)

    ans = 0 
    for x in A:
        ans+=dic[target-x]
        dic[x]+=1
    return ans

    pass

for _ in range(T):

    n = int(input())
    A = list(map(int,input().split()))
    print(check(A))
