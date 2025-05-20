T = int(input())

arr = [ ]
for _ in range(T):
    arr.append(int(input()))
memo = {}

def check(index,s):
    if (index,s) in memo:
        return memo[(index,s)]
    if index==len(arr):
        memo[(index,s)] = (s%360)==0
        return (s%360)==0
    else:
        memo[(index,s)] = check(index+1,s-arr[index]) or check(index+1,s+arr[index])
        return memo[(index,s)]
print("YES" if check(0,0) else "NO")

