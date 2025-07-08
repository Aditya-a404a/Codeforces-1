class SegmentTree:

    def __init__(self,n):
        self.size = 1
        while self.size < n:
            self.size*=2
        self.values = [0]*(self.size*2)
        self.min = [0]*(self.size*2)

    def set(self,node,i,j,val,left,right):
        if i<=left and right<=j:
            self.values[node]+=val
            self.min[node]+=val
            return 
        if j<=left or i>=right:
            return
        mid = (left+right)//2
        self.set(node*2+1,i,j,val,left,mid)
        self.set(node*2+2,i,j,val,mid,right)
        self.min[node] = min(self.min[node*2+1],self.min[node*2+2])+self.values[node]

    def query(self,node,i,j,left,right):
        if i<=left and right<=j:
            return self.min[node]
        if j<=left or i>=right:
            return float('inf')
        mid = (left+right)//2
        q2 = self.query(node*2+1,i,j,left,mid)
        q1 = self.query(node*2+2,i,j,mid,right)
        return min(q1,q2) + self.values[node]
n,m = list(map(int,input().split()))
t = SegmentTree(n)
for _ in range(m):
    q = list(map(int,input().split()))
    if q[0]==1:
        t.set(0,q[1],q[2],q[3],0,t.size)
    else:
        print(t.query(0,q[1],q[2],0,t.size))

        
        





