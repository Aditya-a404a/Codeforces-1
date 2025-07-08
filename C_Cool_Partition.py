n = int(input())
nums = [int(input()) for _ in range(n)]

class SegmentTree:

    def __init__(self, n):
        self.NO = -1
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.operations = [self.NO] * (self.size * 2)
        self.values = [0] * (self.size * 2)

    def propagate(self, node, left, right):
        if self.operations[node] == self.NO:
            return
        if right - left == 1:
            return
        mid = (left + right) // 2
        self.operations[node * 2 + 1] = self.operations[node]
        self.values[node * 2 + 1] = self.operations[node] * (mid - left)
        self.operations[node * 2 + 2] = self.operations[node]
        self.values[node * 2 + 2] = self.operations[node] * (right - mid)
        self.operations[node] = self.NO

    def set(self, node, i, j, val, left, right):
        self.propagate(node, left, right)
        if i >= right or j <= left:
            return
        if i <= left and right <= j:
            self.operations[node] = val
            self.values[node] = (right - left) * val
            return
        mid = (left + right) // 2
        self.set(node * 2 + 1, i, j, val, left, mid)
        self.set(node * 2 + 2, i, j, val, mid, right)
        self.values[node] = self.values[node * 2 + 1] + self.values[node * 2 + 2]

    def query(self, node, i, j, left, right):
        self.propagate(node, left, right)
        if i >= right or j <= left:
            return 0
        if i <= left and right <= j:
            return self.values[node]
        mid = (left + right) // 2
        return self.query(node * 2 + 1, i, j, left, mid) + self.query(node * 2 + 2, i, j, mid, right)

    def get(self, idx):
        return self.query(0, idx, idx + 1, 0, self.size)


tree2 = SegmentTree(n)

for i in range(n):
    tree2.set(0, i, i + 1, nums[i], 0, tree2.size)

m = int(input())
result = 0

for _ in range(m):
    q = list(map(int, input().split()))
    if q[0] == 1:
        l, r = q[1], q[2]
        A_l = tree2.get(l)
        for i in range(l, r + 1):
            val = (i - l + 1) * A_l
            tree2.set(0, i, i + 1, val, 0, tree2.size)
    else:
        l, r = q[1], q[2]
        result+= tree2.query(0, l, r + 1, 0, tree2.size)

print(result)