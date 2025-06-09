class SegmentTree:

    def __init__(self,n):
        self.size = 1
        while self.size < n:
            self.size*=2
        self.values = [ [0]*4 for x in range(2*self.size)]
    
    def _build(self,node,left,right,arr):

        if right-left==1:
            if left < len(arr):
                if arr[left]>=0:
                    self.values[node] = [arr[left],arr[left],arr[left],arr[left]]
                else:
                    self.values[node] = [0,0,0,arr[left]]
            return 
        mid = (left+right)//2
        self._build(node*2+1,left,mid,arr)
        self._build(node*2+2,mid,right,arr)
        x = self.values[node*2+1]
        y = self.values[node*2+2]
        #  merging 
        t = [max(x[0],y[0],x[2]+y[1]),max(x[1],x[3]+y[1]),max(y[2],y[3]+x[2]),y[3]+x[3]]
        self.values[node] = t

    def build(self,arr):
        self._build(0,0,self.size,arr)

    def _set(self,node,idx,val,left,right):
        if right - left==1:
            if val>=0: 
                self.values[node] = [val,val,val,val]
            else:
                self.values[node] = [0,0,0,val]
            return 
        mid = (left+right)//2
        if (idx < mid):
            self._set(node*2+1,idx,val,left,mid)
        else:
            self._set(node*2+2,idx,val,mid,right)
        x = self.values[node*2+1]
        y = self.values[node*2+2]
        #  merging 
        t = [max(x[0],y[0],x[2]+y[1]),max(x[1],x[3]+y[1]),max(y[2],y[3]+x[2]),y[3]+x[3]]
        self.values[node] = t
    
    
    def set(self,idx,val):
        self._set(0,idx,val,0,self.size)

    def _query(self,node,i,j,left,right):
        if i<=left and right<=j:
            return self.values[node]
        if left>=j or i>=right:
            return [-float("inf"),0,0,0,]
        mid = (left+right)//2
        x = self._query(node*2+1,i,j,left,mid)
        y = self._query(node*2+2,i,j,mid,right)
        t = [max(x[0],y[0],x[2]+y[1]),max(x[1],x[3]+y[1]),max(y[2],y[3]+x[2]),y[3]+x[3]]
        return t
    def query(self,i,j):
        return self._query(0,i,j,0,self.size)
    
    
n,m = list(map(int,input().split()))
nums = list(map(int,input().split()))
st = SegmentTree(n)
st.build(nums)
print(st.query(0,n)[0])
for _ in range(m):
    q = list(map(int,input().split()))
    st.set(q[0],q[1])
    print(st.values[0][0])
    
