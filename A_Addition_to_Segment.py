n,m = list(map(int,input().split()))

class SegmentTree:

    def __init__(self,n):
        self.size = 1 
        while self.size  < n :
            self.size*=2
        self.values = [0]*(self.size*2)
    
    def add(self,node,i,j,val,left,right):
        if i<=left and right<=j:
            self.values[node]+=val
            return
        if left>=j or i>=right:
            return
        mid = (left+right)//2
        self.add(node*2+1,i,j,val,left,mid)
        self.add(node*2+2,i,j,val,mid,right)
    def find(self,node,idx,left,right):
        if right-left==1:
            return self.values[node]
        ans = self.values[node]
        mid = (left+right)//2
        if (idx < mid):
            ans+=self.find(node*2+1,idx,left,mid)
        else:
            ans+=self.find(node*2+2,idx,mid,right)
        return ans 

tree = SegmentTree(n)
for _ in range(m):

    q = list(map(int,input().split()))
    if q[0]==1:
        tree.add(0,q[1],q[2],q[3],0,tree.size)
    else:
        print(tree.find(0,q[1],0,tree.size))
