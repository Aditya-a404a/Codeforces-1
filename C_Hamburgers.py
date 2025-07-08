recipe = input()
nb,ns,nc = list(map(int,input().split()))
pb,ps,pc = list(map(int,input().split()))
r = int(input())
left = 0 
right = 10**13
from collections import defaultdict
dic = defaultdict(int)
for x in recipe:
    dic[x]+=1
def good(mid,dic,pb,ps,pc,nb,ns,nc):
    if r >= pb*max(0,dic["B"]*mid-nb)+ps*max(0,dic["S"]*mid-ns)+pc*max(0,dic["C"]*mid-nc):
        return True
    else:
        return False
    pass

while left<=right:
    mid = (left+right)//2
    if good(mid,dic,pb,ps,pc,nb,ns,nc):
        left = mid + 1 
    else:
        right = mid - 1 
print(right)
