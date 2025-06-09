class SegmentTree:
    def __init__(self, n):
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.tree = [0] * (2 * self.size)

    def build(self,node,left,right,arr):
        if right-left==1:
            if left<len(arr):
                self.tree[node] = arr[left]
            return
        mid = (left+right)//2
        self.build(node*2+1,left,mid,arr)
        self.build(node*2+2,mid,right,arr)
        self.tree[node] = self.tree[node*2+1] + self.tree[node*2+2]

        



        

    def _set(self, idx, value, node, left, right):
        if right - left == 1:
            self.tree[node] = value
            return
        mid = (left + right) // 2
        if idx < mid:
            self._set(idx, value, 2 * node + 1, left, mid)
        else:
            self._set(idx, value, 2 * node + 2, mid, right)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def set(self, idx, value):
        self._set(idx, value, 0, 0, self.size)

    def _query(self, node, i, j, left, right):
        if left >= j or right <= i:
            return 0
        if i <= left and right <= j:
            return self.tree[node]
        mid = (left + right) // 2
        s1 = self._query(2 * node + 1, i, j, left, mid)
        s2 = self._query(2 * node + 2, i, j, mid, right)
        return s1 + s2

    def query(self, i, j):
        return self._query(0, i, j, 0, self.size)

# Input and operations
n, m = map(int, input().split())
nums = list(map(int, input().split()))
st = SegmentTree(n)
st.build(0,0,st.size,nums)
for _ in range(m):
    q = list(map(int, input().split()))
    if q[0] == 1:
        st.set(q[1], q[2])
    else:
        print(st.query(q[1], q[2]))



        
