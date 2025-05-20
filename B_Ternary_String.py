T = int(input())

def check(s):
    s = list(s)

    s = [int(x) for x in s]

    c = [0]*3
    l = 0
    best = 2**32 
    for i in range(len(s)):
        c[s[i]-1]+=1
        while c[0] >= 1 and  c[1] >= 1 and c[2] >= 1:
            best = min(best, i-l+1)
            c[s[l]-1]-=1
            l+=1
    return best if best != 2**32 else 0


for _ in range(T):
    a = input()
    print(check(a))