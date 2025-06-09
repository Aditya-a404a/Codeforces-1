s = input()

count = [0]*26
dp = [ [0]*26 for x in range(26)]

for x in s:
    c = ord(x)-97
    for y in range(26):
        dp[y][c]+=count[y]
    count[c]+=1

print(max(max(count),max(max(x) for x in dp)))

    