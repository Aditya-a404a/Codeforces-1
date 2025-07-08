n,m = list(map(int,input().split()))

nums = list(map(int,input().split()))

class SegmentTree:

    def __init__(self,n):
        self.size = 1 
        while self.size < n :
            self.size*=2
        self.values = [[[0]*40,0] for x in range(self.size*2)]
    def build(self,node,left,right,arr):
        if right-left==1:
            if left < len(arr):
                self.values[node][0][arr[left]]+=1
            return
        mid = (left+right)//2
        self.build(node*2+1,left,mid,arr)
        self.build(node*2+2,mid,right,arr)
        for x in range(41):
            self.values[node][x]+=self.values[node*2+1][x]+self.values[node*2+2]
    def _set(self,node,idx,val,left,right):
        if right-left==1:
            for x in range(41):
                if self.values[node][0][x]==1:
                    self.values[node][0][x]=0
                    break
            self.values[node][0][val]+=1
            return 
        mid = (left+right)//2
        if idx<mid:
            self._set(node*2+1,idx,val,left,mid)
        else:
            self._set(node*2+2,idx,val,mid,right)
        for x in range(41):
            self.values[node][x]+=self.values[node*2+1][x]+self.values[node*2+2]
    # def query()

        

