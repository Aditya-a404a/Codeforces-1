T = int(input())

def maxsub(a):
    # assume len(a) >= 1
    current_max = global_max = a[0]
    for x in a[1:]:
        # either start fresh at x, or extend the previous subarray
        current_max = max(x, current_max + x)
        # keep track of the best we’ve ever seen
        global_max = max(global_max, current_max)
    return global_max
def check(A):

    s = sum(A)
    m = max(maxsub(A[1:]),maxsub(A[:len(A)-1]))
    

    
    if m < s:
        return "YES"
    return "NO"


    pass
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(check(A))
    pass