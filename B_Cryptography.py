r,n,m  = list(map(int,input().split()))
def multiply_2x2_matrices(A, B):
    if len(A) != 2 or len(A[0]) != 2 or len(B) != 2 or len(B[0]) != 2:
        raise ValueError("Both matrices must be 2x2")
    result = [
        [
            (A[0][0]*B[0][0] + A[0][1]*B[1][0])%r,
            (A[0][0]*B[0][1] + A[0][1]*B[1][1])%r
        ],
        [
            (A[1][0]*B[0][0] + A[1][1]*B[1][0])%r,
            (A[1][0]*B[0][1] + A[1][1]*B[1][1])%r
        ]
    ]
    return result
class SegmentTree:

    def __init__(self,n):
        self.size = 1
        while self.size < n :
            self.size*=2
        self.values = [ [[1,0],[0,1]] for x in range(2*self.size)]
    
    def build(self,node,left,right,arr):
        if right-left==1:
            if left < len(arr):
                self.values[node] = arr[left]
            return 
        mid = (left+right)//2
        self.build(node*2+1,left,mid,arr)
        self.build(node*2+2,mid,right,arr)
        self.values[node] = multiply_2x2_matrices(self.values[node*2+1],self.values[node*2+2])
    
    def set(self,node,idx,val,left,right):
        if right-left==1:
            self.values[node] =  val
            return
        mid = (left+right)//2
        if idx < mid :
            self.set(node*2+1,idx,val,left,mid)
        else:
            self.set(node*2+2,idx,val,mid,right)
        self.values[node] = multiply_2x2_matrices(self.values[node*2+1],self.values[node*2+2])
    
    def query(self,node,i,j,left,right):
        if i<=left and right<=j:
            return self.values[node]
        if i>=right or j<=left:
            return [[1,0],[0,1]]
        mid = (left+right)//2
        q1 = self.query(node*2+1,i,j,left,mid)
        q2 = self.query(node*2+2,i,j,mid,right)
        return multiply_2x2_matrices(q1,q2)
arr = [ ]
for _ in range(n):
    t = [ ]
    for x in range(2):
        t.append(list(map(int,input().split())))
    arr.append(t)
    input()
tree = SegmentTree(n)
tree.build(0,0,tree.size,arr)
for _ in range(m):
    q = list(map(int,input().split()))
    t = tree.query(0,q[0]-1,q[1],0,tree.size)
    for x in t:
        print(*x)
    print()
    
        
