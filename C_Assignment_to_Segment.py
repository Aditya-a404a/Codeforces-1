# n,m = list(map(int,input().split()))


# class SegmentTree:

#     def __init__(self,n):
#         self.size = 1 
#         while self.size < n:
#             self.size*=2
#         self.values = [0]*(self.size*2)
#         self.NOO = float("inf")
#     def propagate(self,node,left,right):
#         if right-left==1:
#             return 
#         if self.values[node]!=self.NOO:
#             self.values[node*2+1] = self.values[node]
#             self.values[node*2+2] = self.values[node]
#         self.values[node] = self.NOO
#     def add(self,node,val,i,j,left,right):
#         self.propagate(node,left,right)
#         if i<=left and right<=j:
#             self.values[node] = val
#             return 
#         if j<=left or i>=right:
#             return 
#         mid = (left+right)//2
#         self.add(node*2+1,val,i,j,left,mid)
#         self.add(node*2+2,val,i,j,mid,right)
    
#     def find(self,node,idx,left,right):
#         self.propagate(node,left,right)
#         if right-left==1:
#             return self.values[node]
#         mid = (left+right)//2
#         if idx < mid:
#             return self.find(node*2+1,idx,left,mid)
#         return self.find(node*2+2,idx,mid,right)
# tree = SegmentTree(n)
# for _ in range(m):
#     q = list(map(int,input().split()))
#     if q[0]==1:
#         tree.add(0,q[-1],q[1],q[2],0,tree.size)
#     else:
#         print(tree.find(0,q[1],0,tree.size))
from heapq import  heappush,heappop
from collections import defaultdict
def solve(pages,threshold):

    dic = defaultdict(list)
    for x,y in zip(pages,threshold):
        dic[y].append(x)
    ans = 0 
    for x in dic.keys():
        dic[x].sort(reverse = True)
        ans+=sum(dic[x][:min(x,len(dic[x]))])
    return ans 

print(solve([2,6,10,13], [2,1,1,1]))
        
    



