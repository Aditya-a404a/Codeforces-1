T = int(input())

from collections import defaultdict
def solve():
    n = int(input())
    nums = [ ]
    for x in range(n):
        nums.append(x%4)
    count = defaultdict(int)
    for x in nums:
        count[x]+=1
    
    if (count[3]>count[0] or count[0]>count[3] or count[1]>count[2] or count[2]>count[1]):
        print("Alice")
    else:
        print("Bob")
    
    




    pass
for _ in range(T):

    solve()