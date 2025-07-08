n = int(input())

nums = list(map(int,input().split()))

class SegmentTree:
    def __init__(self,n):
        self.size = 1
        while self.size  < n :
            self.size*=2
        self.values = [ 0 for x in range(self.size*2)]
    def build(self,node,left,right,nums):
        if right-left==1:
            if left < len(nums):
                self.values[node] = nums[left]
            return 
        mid = (left+right)//2
        self.build(node*2+1,left,mid,nums)
        self.build(node*2+2,mid,right,nums)
        self.values[node] = self.values[node*2+1]+self.values[node*2+2]
    def _set(self,node,idx,value,left,right):
        if right-left==1:
            self.values[node]  = value
            return
        mid = (left+right)//2
        if (idx < mid):
            self._set(node*2+1,idx,value,left,mid)
        else:
            self._set(node*2+2,idx,value,mid,right)
        self.values[node] = self.values[node*2+1]+self.values[node*2+2]
    def query(self,node,i,j,left,right):
        if i<=left and right<=j:
            return self.values[node] 
        if i>=right or j<=left:
            return 0
        mid = (left+right)//2 
        return self.query(node*2+1,i,j,left,mid)+self.query(node*2+2,i,j,mid,right)
odd = SegmentTree(n)
even = SegmentTree(n)
o = []
e = []
for x in range(len(nums)):
    if x%2==0:
        e.append(nums[x])
        o.append(0)
    else:
        e.append(0)
        o.append(nums[x])
odd.build(0,0,odd.size,o)
even.build(0,0,even.size,e)
m = int(input())
for _ in range(m):
    q = list(map(int,input().split()))
    if q[0]==0:
        if (q[1]-1)%2==0:
            even._set(0,q[1]-1,q[2],0,even.size)
        else:
            odd._set(0,q[1]-1,q[2],0,odd.size)
    else:
        if (q[1]-1)%2==0:
            print((even.query(0,q[1]-1,q[2],0,even.size)-odd.query(0,q[1]-1,q[2],0,odd.size)))
        else:
            print(-(even.query(0,q[1]-1,q[2],0,even.size)-odd.query(0,q[1]-1,q[2],0,odd.size)))

    

