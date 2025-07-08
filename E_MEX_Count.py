# class SegmentTree:

#     def __init__(self,n,arr):
#         self.size = 1 
#         self.NO = None
#         while self.size < n :
#             self.size*=2
#         self.operation = [self.NO]*(self.size*2)
#         self.values = [0]*(self.size*2) 
#         self.increment = [self.NO]*(self.size*2) 
#         self.build(0,0,self.size,arr)
    
#     def propagate(self,node,left,right):
#         if right-left==1:
#             return
#         if self.operation[node]==self.NO :
#             return 
#         mid = (left+right)//2
#         self.operation[node*2+1] = self.operation[node] 
#         self.values[node*2+1] = (mid-left)*self.operation[node]
#         self.operation[node*2+2] = self.operation[node]
#         self.values[node*2+2] = (right-mid)*self.operation[node]
#         self.operation[node] = self.NO
#         self.increment[node*2+1] = self.increment[node]
#         self.values[node*2+1]+= (self.increment[node]*(mid-left)*(mid+left-1))//2
#         self.increment[node*2+2] = self.increment[node]
#         self.values[node*2+2] = (self.increment[node]*(right-mid)*(right+mid-1))//2
#         self.increment[node] = self.NO
#         return 

    
#     def build(self,node,left,right,arr):
#         if right-left==1:
#             if left < len(arr):
#                 self.values[node] = arr[left]
#             return 
#         mid = (left+right)//2
#         self.build(node*2+1,left,mid,arr)
#         self.build(node*2+2,mid,right,arr)
#         self.values[node] = self.values[node*2+1]+self.values[node*2+2]
    
#     def set(self,node,i,j,val,inc,left,right):
#         self.propagate(node,left,right)
#         if i<=left and right<=j:
#             self.operation[node] = val
#             self.values[node] =  (right-left)*val
#             self.increment[node] = inc
#             self.values[node]+=(((right-left)*(right+left-1))//2)*inc
#             return
#         if i>=right or j<=left:
#             return 
#         mid = (left+right)//2
#         self.set(node*2+1,i,j,val,inc,left,mid)
#         self.set(node*2+2,i,j,val,inc,mid,right)
#         self.values[node] = self.values[node*2+1]+self.values[node*2+2]
#         return 
#     def query(self,node,i,j,left,right):
#         self.propagate(node,left,right)
#         if i<=left and right<=j:
#             return self.values[node]
#         if i>=right or j<=left:
#             return  0 
#         mid = (left+right)//2
#         q1 = self.query(node*2+1,i,j,left,mid)
#         q2 = self.query(node*2+2,i,j,mid,right)
#         return q1+q2

# n = int(input())
# nums = [ ]
# for x in range(n):
#     nums.append(int(input()))
# q = int(input())
# tree = SegmentTree(n,nums)
# count = 0 
# for t in range(q):
#     t,x,y= list(map(int,input().split()))
#     if t==1:
#         val  = tree.query(0,x,x+1,0,tree.size)
#         a = val*(1-x)
#         b = val 
#         tree.set(0,x,y+1,a,b,0,tree.size)
#     else:
#         count+=tree.query(0,x,y+1,0,tree.size)
# print(count)

import sys

def main():
    input = sys.stdin.readline
    MOD = 10**9 + 7
    INF_NEG = -10**30

    n = int(input())
    X = int(input())-1
    Y = int(input())-1
    Z = int(input())-1
    A = [int(input()) for _ in range(n)]
    B = [int(input()) for _ in range(n)]

    # dp[u][d] = best sum after i ops with u uses, d of them type-2
    # we only need dimensions up to Y uses and up to X type-2's each row
    dp = [[INF_NEG]*(Y+1) for _ in range(Y+1)]
    dp[0][0] = 0

    for i in range(1, n+1):
        ai, bi = A[i-1], B[i-1]

        # 1) apply the "subtract B" choice to all existing states
        for u in range(0, min(i, Y)+1):
            for d in range(0, min(u, X)+1):
                dp[u][d] -= bi

        # 2) consider taking one more "use" (u from high→low)
        #    so we pull transitions from dp[u-1][*] into dp[u][*]
        for u in range(min(i, Y), 0, -1):
            y_factor = Y - (u-1)
            # we update d from high→0 so we don't clobber dp[u-1][*]
            for d in range(min(u, X), -1, -1):

                # a) type-3: don't change d
                base = dp[u-1][d]
                # z left = Z - ((u-1)-d)
                rem_z = Z - ((u-1) - d)
                if base > INF_NEG and rem_z >= 1:
                    gain = ai * (X - d) * y_factor * rem_z
                    dp[u][d] = max(dp[u][d], (base + gain) % MOD)

                # b) type-2: increase d by 1 (so require d>=1 here and use dp[u-1][d-1])
                if d >= 1:
                    base2 = dp[u-1][d-1]
                    rem_x = X - (d-1)
                    rem_z2 = Z - ((u-1) - (d-1))
                    if base2 > INF_NEG and rem_x >= 1:
                        gain2 = ai * rem_x * y_factor * (Z - (u-1 - (d-1)))
                        dp[u][d] = max(dp[u][d], (base2 + gain2) % MOD)

    # answer is the best over all valid (u,d)
    ans = INF_NEG
    for u in range(0, Y+1):
        for d in range(0, min(u, X)+1):
            ans = max(ans, dp[u][d])
    print(ans % MOD)


if __name__ == "__main__":
    main()






    



