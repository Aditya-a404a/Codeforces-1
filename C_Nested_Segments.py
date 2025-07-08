n = int(input())
arr = list(map(int,input().split()))
from collections import defaultdict

class SegmentTree:

    def __init__(self,n):
        self.size = 1
        while self.size < n:
            self.size*=2
        self.values = [0]*(2*self.size)
    
    def _set(self,node,idx,left,right):
        if right - left == 1:
            self.values[node]=1
            return
        mid = (left+right)//2
        if (idx < mid):
            self._set(node*2+1,idx,left,mid)
        else:
            self._set(node*2+2,idx,mid,right)
        self.values[node] = self.values[node*2+1]+self.values[node*2+2]
    
    def set(self,idx):
        self._set(0,idx,0,self.size)
    
    def query(self,node,i,j,left,right):
        if i<=left and right<=j:
            return self.values[node]
        if j<=left or i>=right:
            return 0 
        mid = (left+right)//2
        return self.query(node*2+1,i,j,left,mid)+self.query(node*2+2,i,j,mid,right)

tree = SegmentTree(2*n)

dic = defaultdict(lambda : -1)
ans = [0]*n
for x in range(len(arr)):

    if dic[arr[x]]!=-1:
        ans[arr[x]-1]=tree.query(0,dic[arr[x]],x,0,tree.size)
        tree.set(dic[arr[x]])
    else:
        dic[arr[x]] = x
print(*ans)


