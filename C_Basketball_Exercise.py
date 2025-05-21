n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
dp = [ [0]*2 for x in range(n+1)]
dp[1][0] = A[0]
dp[1][1] = B[0]

for x in range(2,len(dp)):
    dp[x][1] = max(dp[x-1][0]+B[x-1],dp[x-1][1])
    dp[x][0] = max(dp[x-1][1]+A[x-1],dp[x-1][0])
print(max(max(x) for x in dp ))