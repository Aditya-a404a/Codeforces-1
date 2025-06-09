
class SegmentTree:
    size = 1 
    def __init__(self,n):
        while self.size<n:
            self.size*=2
        self.values = [float("inf")]*(2*self.size)
    
    def build(self,node,arr,left,right):
        if right-left==1:
            if left < len(arr):
                self.values[node]=arr[left]
            return
        mid = (left+right)//2
        self.build(node*2+1,arr,left,mid)
        self.build(node*2+2,arr,mid,right)
        self.values[node] = min(self.values[node*2+1],self.values[node*2+2])


    def _set(self,idx,value,node,left,right):
        if right-left==1:
            self.values[node]=value
            return
        mid = (left+right)//2
        if (idx<mid):
            self._set(idx,value,node*2+1,left,mid)
        else:
            self._set(idx,value,node*2+2,mid,right)
        self.values[node] = min(self.values[node*2+1],self.values[node*2+2])

    def set(self,idx,value):
        self._set(idx,value,0,0,self.size)
    
    def _query(self,node,i,j,left,right):
        if i>=right or left>=j:
            return float('inf')
        if i <= left and right <= j:
            return self.values[node]
        mid = (left+right)//2
        s1 = self._query(node*2+1,i,j,left,mid)
        s2 = self._query(node*2+2,i,j,mid,right)
        return min(s1,s2)
    def query(self,i,j):
        return self._query(0,i,j,0,self.size)
n,q = list(map(int,input().split()))
nums = list(map(int,input().split()))
st = SegmentTree(n)
st.build(0,nums,0,st.size);

for _ in range(q):
    t = list(map(int,input().split()))
    if t[0]==2:
        print(st.query(t[1],t[2]))
    else:
        st.set(t[1],t[2])
    

        