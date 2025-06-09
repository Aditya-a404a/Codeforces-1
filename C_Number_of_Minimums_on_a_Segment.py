class SegmentTree:

    def __init__(self,n):
        self.size = 1 
        while self.size<n:
            self.size*=2
        self.values = [[float('inf'),0] for x in range(2*self.size)]
    
    def build(self,node,left,right,arr):
        if right-left==1:
            if left < len(arr):
                self.values[node] = [arr[left],1]
            return
        mid = (left+right)//2
        self.build(node*2+1,left,mid,arr)
        self.build(node*2+2,mid,right,arr)
        if self.values[node*2+1][0] > self.values[node*2+2][0]:
            self.values[node] = self.values[node*2+2]
        elif self.values[node*2+1][0] < self.values[node*2+2][0]:
            self.values[node] = self.values[node*2+1]
        else:
            self.values[node] = [self.values[node*2+1][0],self.values[node*2+2][1]+self.values[node*2+1][1]]
    
    def _set(self,node,idx,value,left,right):
        if right-left==1:
            self.values[node]=[value,1]
            return
        mid = (left+right)//2
        if idx<mid:
            self._set(node*2+1,idx,value,left,mid)
        else:
            self._set(node*2+2,idx,value,mid,right)
        if self.values[node*2+1][0] > self.values[node*2+2][0]:
            self.values[node] = self.values[node*2+2]
        elif self.values[node*2+1][0] < self.values[node*2+2][0]:
            self.values[node] = self.values[node*2+1]
        else:
            self.values[node] = [self.values[node*2+1][0],self.values[node*2+2][1]+self.values[node*2+1][1]]
        
    def set(self,idx,value):
        self._set(0,idx,value,0,self.size)

    def _query(self,node,i,j,left,right):
        if i<=left and right<=j:
            return self.values[node]
        if left>=j or right<=i:
            return [float('inf'),0]
        mid = (left+right)//2
        s1 = self._query(node*2+1,i,j,left,mid)
        s2 = self._query(node*2+2,i,j,mid,right)
        if s1[0] < s2[0]:
            return s1
        elif s1[0] > s2[0]:
            return s2
        else:
            return [s1[0],s1[1]+s2[1]]
    def query(self,i,j):
        return self._query(0,i,j,0,self.size)

n,m = list(map(int,input().split()))

nums = list(map(int,input().split()))

st = SegmentTree(n)
st.build(0,0,st.size,nums)
for _ in range(m):
    q = list(map(int,input().split()))
    if q[0]==2:
        print(*st.query(q[1],q[2]))
    else:
        st.set(q[1],q[2])
    

            