n = int(input())
arr = list(map(int,input().split()))

class SegmentTree:

    def __init__(self,n):
        self.size = 1
        while self.size < n :
            self.size*=2
        self.values = [0]*(self.size*2)
    
    def _set(self,node,idx,left,right):
        if right-left==1:
            self.values[node] = 1
            return 

        mid = (left+right)//2
        if (idx < mid):
            self._set(node*2+1,idx,left,mid)
        else:
            self._set(node*2+2,idx,mid,right)
        self.values[node] =  self.values[node*2+1] + self.values[2*node+2]
    
    def set(self,idx):
        self._set(0,idx,0,self.size)
    
    def _query(self,node,i,j,left,right):
        if i<=left and right<=j:
            return self.values[node]
        if left>=j or i>=right:
            return 0 
        mid = (left+right)//2
        ans = self._query(node*2+1,i,j,left,mid)+self._query(node*2+2,i,j,mid,right)
        return ans 
    def query(self,idx):
        return self._query(0,idx+1,self.size,0,self.size)
   
    
tree = SegmentTree(max(arr)+1)
ans = []
for x in arr:
    ans.append(tree.query(x)) 
    tree.set(x)
print(*ans)




        


