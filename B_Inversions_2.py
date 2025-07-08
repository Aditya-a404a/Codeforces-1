n = int(input())
nums = list(map(int,input().split()))

class SegmentTree:

    def __init__(self,n):
        self.size = 1 
        while self.size < n:
            self.size*=2
        self.values = [0]*(self.size*2)
    
    def build(self,node,left,right,arr):
        if right-left==1:
            if left < len(arr):
                self.values[node] = 1
            return
        mid = (left+right)//2
        self.build(node*2+1,left,mid,arr)
        self.build(node*2+2,mid,right,arr)
        self.values[node] = self.values[node*2+1]+self.values[node*2+2]

    def _set(self,node,idx,value,left,right):
        if right-left==1:
            self.values[node] = value
            return
        mid = (left+right)//2
        if (idx < mid ):
            self._set(node*2+1,idx,value,left,mid)
        else:
            self._set(node*2+2,idx,value,mid,right)
        self.values[node] = self.values[node*2+1]+self.values[node*2+2]
    
    def set(self,idx,value):
        self._set(0,idx,value,0,self.size)
    
    def query(self,node,left,right,k):
        if right-left==1:
            return left
        mid = (left+right)//2
        R = self.values[node*2+2]
        if R > k:
            return self.query(node*2+2,mid,right,k)
        return self.query(node*2+1,left,mid,k-R)
tree = SegmentTree(n)
tree.build(0,0,tree.size,[ 1 for x in range(n)])

ans = []
for t in nums[::-1]:
    # total remaining free slots
    idx = tree.query(0, 0, tree.size, t)
    ans.append(idx+1)
    tree.set(idx, 0)
print(*ans[::-1])

    

        
    
