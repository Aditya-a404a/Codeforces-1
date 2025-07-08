import sys
input = sys.stdin.readline

T = int(input())

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    
    p = [float('inf')]
    for x in nums:
        p.append(min(p[-1], x))
    
    s = [float('-inf')]
    for x in reversed(nums):
        s.append(max(s[-1], x))
    s = s[1:][::-1]
    p = p[1:]

    ans = []
    for i, x in enumerate(nums):
        if x == p[i] or x == s[i]:
            ans.append('1')
        else:
            ans.append('0')
    
    print(''.join(ans))

for _ in range(T):
    solve()


