mod = 10**9+7

class SegmentTree:
    def __init__(self,n):
        self.size = 1 
        while self.size < n:
            self.size*=2
        self.values = [1]*(self.size*2)
        self.sum = [1]*(self.size*2)
    def build(self,node,left,right):
        if right-left==1:
            self.values[node]=1 
            self.sum[node]=1
            return 
        mid = (left+right)//2
        self.build(node*2+1,left,mid)
        self.build(node*2+2,mid,right)
        self.sum[node] = (self.sum[node*2+1]+self.sum[node*2+2])%mod
    def operation(self,node,i,j,val,left,right):
        if i<=left and right<=j:
            self.values[node]*=val
            self.sum[node]*=val
            self.values[node]%=mod
            self.sum[node]%=mod
            return 
        if i>=right or j<=left:
            return 
        mid = (left+right)//2
        self.operation(node*2+1,i,j,val,left,mid)
        self.operation(node*2+2,i,j,val,mid,right)
        self.sum[node] = ((self.sum[node*2+1]+self.sum[node*2+2])*self.values[node])%mod
    def query(self,node,i,j,left,right):
        if i<=left and right<=j:
            return self.sum[node]
        if i>=right or j<=left:
            return 0 
        mid = (left+right)//2

        q = self.query(node*2+1,i,j,left,mid)
        q1 = self.query(node*2+2,i,j,mid,right)
        return ((q+q1)*self.values[node])%mod

n,m = list(map(int,input().split()))

tree = SegmentTree(n)
tree.build(0,0,tree.size)

for x in range(m):
    
    q = list(map(int,input().split()))
    if q[0]==1:
        tree.operation(0,q[1],q[2],q[3],0,tree.size)
    else:
        print(tree.query(0,q[1],q[2],0,tree.size))


        