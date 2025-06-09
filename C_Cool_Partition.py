import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = 0
    prev_set = set()    
    i = 0               
    
    while i < n:
        
        needed = {x: True for x in prev_set}
        remain = len(needed)
        
       
        j = i
        if remain > 0:
            while j < n and remain > 0:
                v = a[j]
                if needed.get(v, False):
                    needed[v] = False
                    remain -= 1
                j += 1
            
            if remain > 0:
                break
            segment_end = j - 1
        else:
            
            segment_end = i
        
       
        ans += 1
        prev_set = set(a[i:segment_end+1])
        i = segment_end + 1
    print(ans)

# driver
T = int(input())
for _ in range(T):
    solve()
