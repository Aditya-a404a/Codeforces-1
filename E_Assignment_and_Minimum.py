class SegmentTree:

    def __init__(self,n):
        self.NO_operation = float("inf") 
        self.size = 1 
        while self.size < n :
            self.size*=2
        self.operations = [0]*(self.size*2)
        self.min = [0]*(self.size*2)
    def propagate(self,node,left,right):
        if self.operations[node]==self.NO_operation:
            return
        if right-left==1:
            return
        self.operations[node*2+1] = self.operations[node]
        self.min[node*2+1] = self.operations[node*2+1]
        self.operations[node*2+2] = self.operations[node]
        self.min[node*2+2] = self.operations[node*2+2]
        self.operations[node] = self.NO_operation

    def apply(self,node,i,j,val,left,right):
        self.propagate(node,left,right)
        if i<=left and right<=j:
            self.operations[node]=val
            self.min[node]=val
            return
        if i>=right or j<=left:
            return
        mid = (left+right)//2
        self.apply(node*2+1,i,j,val,left,mid)
        self.apply(node*2+2,i,j,val,mid,right)
        self.min[node] =  min(self.min[node*2+1],self.min[2*node+2])
    def query(self,node,i,j,left,right):
        self.propagate(node,left,right)
        if i<=left and right<=j:
            return self.min[node]
        if i>=right or j<=left:
            return float("inf")
        mid = (left+right)//2
        q = self.query(node*2+1,i,j,left,mid)
        q1 = self.query(node*2+2,i,j,mid,right)
        return min(q,q1)
n,m = list(map(int,input().split()))

tree = SegmentTree(n)

for x in range(m):

    q = list(map(int,input().split()))
    if q[0]==1:
        tree.apply(0,q[1],q[2],q[3],0,tree.size)
    else:
        print(tree.query(0,q[1],q[2],0,tree.size))


