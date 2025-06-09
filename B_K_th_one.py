class SegementTree:

    def __init__(s,n):
        s.size = 1 
        while s.size < n:
            s.size*=2
        s.values = [ 0 for x in range(2*s.size)]
    
    def _build(s,node,left,right,arr):
        if right-left==1:
            if left < len(arr):
                s.values[node] = arr[left]
            return
        mid = (left+right)//2 
        s._build(node*2+1,left,mid,arr)
        s._build(node*2+2,mid,right,arr)
        s.values[node] = s.values[node*2+1]+s.values[node*2+2]

    def build(s,arr):
        s._build(0,0,s.size,arr)
    
    def _set(s,node,idx,value,left,right):
        if right-left==1:
            s.values[node] = value
            return
        mid = (left+right)//2
        if (idx < mid):
            s._set(node*2+1,idx,value,left,mid)
        else:
            s._set(node*2+2,idx,value,mid,right)
        s.values[node] = s.values[node*2+1]+s.values[node*2+2]
    
    def set(s,idx,val):
        s._set(0,idx,val,0,s.size)
    
    def find_kth(self, k, node=0, left=0, right=None):
        """
        Find the smallest index `idx` such that
        sum(arr[0..idx]) > k (0-based k).
        If you want the 1-based k-th '1', call with k-1.
        """
        if right is None:
            right = self.size

        # If we're at a leaf, that's our answer
        if right - left == 1:
            return left

        mid = (left + right) // 2
        left_sum = self.values[node*2 + 1]

        if left_sum > k:
            # The k-th one lies in the left subtree
            return self.find_kth(k, node*2 + 1, left, mid)
        else:
            # It lies in the right subtree; subtract what we skip
            return self.find_kth(k - left_sum, node*2 + 2, mid, right)
n , m = list(map(int,input().split()))
nums = list(map(int,input().split()))
st = SegementTree(n)
st.build(nums)
for _ in range(m):
    q = list(map(int,input().split()))
    if q[0]==1:
        st.set(q[1],abs(1-nums[q[1]]))
        nums[q[1]] = abs(1-nums[q[1]])
    else:
        print(st.find_kth(q[1]))