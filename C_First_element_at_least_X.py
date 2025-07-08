class SegmentTree:

    def __init__(self,n):
        self.size = 1 
        while self.size < n:
            self.size*=2
        self.values = [-float('inf')]*(2*self.size)
    def _build(self,node,left,right,arr):
        if right-left==1:
            if left < len(arr):
                self.values[node] = arr[left]
            return
        mid = (left+right)//2
        self._build(node*2+1,left,mid,arr)
        self._build(node*2+2,mid,right,arr)
        self.values[node] = max(self.values[node*2+1],self.values[node*2+2])
    def build(self,nums):
        self._build(0,0,self.size,nums)
    
    def _set(self,node,idx,val,left,right):
        if right-left==1:
            self.values[node]=val
            return
        mid = (left+right)//2
        if (idx < mid):
            self._set(node*2+1,idx,val,left,mid)
        else:
            self._set(node*2+2,idx,val,mid,right)
        self.values[node] = max(self.values[node*2+1],self.values[node*2+2])
    
    def set(self,idx,value):
        self._set(0,idx,value,0,self.size)
    
    def query(self,node,val,i,left,right):
        if right <= i :
            return -1 
        if right - left==1:
            if self.values[node]>=val:
                return left
            return -1
        mid = (left+right)//2
        a = -1 
        if self.values[node*2+1]>=val:
            return self.query(node*2+1,val,i,left,mid)
        
        if self.values[node*2+2]>=val:
            return  self.query(node*2+2,val,i,mid,right)
        return -1
            
        

    def findfirst(self,x,left):
        return self.query(0,x,left,0,self.size)

n , m = list(map(int,input().split()))

nums = list(map(int,input().split()))

st = SegmentTree(n)
st.build(nums)

for _ in range(m):
    q = list(map(int,input().split()))
    if q[0]==2:
        print(st.findfirst(q[1],0))
    else:
        st.set(q[1],q[2])



    



     