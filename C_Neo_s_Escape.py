class Union:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        
        xp = self.find(x)
        yp = self.find(y)
        if xp == yp:
            return 
        if self.rank[xp] >= self.rank[yp]:
            self.parent[yp] = xp
            self.rank[xp] += self.rank[yp]
        else:
            self.parent[xp] = yp
            self.rank[yp] += self.rank[xp]
        return
        
            

T =  int(input())
def solve(n,arr):
    seen = Union(n)

    for i in range(1,n):
        if abs(arr[i] - arr[i-1])<=1:
            seen.union(i,i-1)
    ans = set([seen.find(x) for x in range(n)])
    return len(ans)


for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(n,arr))