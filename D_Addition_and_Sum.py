class SegmentTree:

    def __init__(self,n):
        self.size = 1
        while self.size < n :
            self.size*=2
        self.operations = [0]*(self.size*2)
        self.values = [0]*(self.size*2)

    def apply(self,node,i,j,val,left,right):
        if i<=left and right<=j:
            self.operations[node]+=val
            self.values[node]+=val*(right-left)
            return 
        if i>=right or j<=left:
            return
        mid = (left+right)//2
        self.apply(node*2+1,i,j,val,left,mid)
        self.apply(node*2+2,i,j,val,mid,right)
        self.values[node] = self.values[node*2+1]+self.values[node*2+2]+(right-left)*self.operations[node]

    def query(self,node,i,j,left,right):
        if i<=left and right<=j:
            return self.values[node]
        if i>=right or j<=left:
            return 0
        mid = (left+right)//2
        q = self.query(node*2+1,i,j,left,mid)
        q2 = self.query(node*2+2,i,j,mid,right)
        return  (q+q2)+self.operations[node]*(min(right,j)-max(left,i))
n,m = list(map(int,input().split()))
tree = SegmentTree(n)
for x in range(m):
    q  = list(map(int,input().split()))
    if q[0]==1:
        tree.apply(0,q[1],q[2],q[3],0,tree.size)
    else:
        print(tree.query(0,q[1],q[2],0,tree.size))



    
