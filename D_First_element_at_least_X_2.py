class SegmentTree:

    def __init__(self,n):
        self.size = 1 
        while self.size < n:
            self.size*=2
        self.values = [-float('inf')]*(2*self.size)

    def _build(self,node,left,right,nums):
        if right-left==1:
            if left< len(nums):
                self.values[node]=nums[left]
            return 
        mid = (left+right)//2
        self._build(node*2+1,left,mid,nums)
        self._build(node*2+2,mid,right,nums)
        self.values[node] = max(self.values[node*2+1],self.values[node*2+2])
    
    def _set(self,node,idx,val,left,right):
        if right-left==1:
            self.values[node] = val
            return
        mid = (left+right)//2
        if (idx < mid):
            self._set(node*2+1,idx,val,left,mid)
        else:
            self._set(node*2+2,idx,val,mid,right)
        self.values[node] = max(self.values[node*2+1],self.values[node*2+2])

    def set(self,idx,val):
        self._set(0,idx,val,0,self.size)

    def query(self,node,val,start,left,right):
        if right<=start:
            return -1
        if self.values[node]<val:
            return -1 
        if right-left==1:
            return left
        mid = (left+right)//2
        a = self.query(node*2+1,val,start,left,mid)
        if a!=-1:
            return a 
        return self.query(node*2+2,val,start,mid,right)
    
    def findx(self,x,start=0):
        return self.query(0,x,start,0,self.size)
    def build(self,nums):
        self._build(0,0,self.size,nums)
n,m = list(map(int,input().split()))
nums = list(map(int,input().split()))

st = SegmentTree(n)
st.build(nums)
for _ in range(m):
    q = list(map(int,input().split()))
    if q[0]==2:
        print(st.findx(q[1],q[2]))
    else:
        st.set(q[1],q[2])