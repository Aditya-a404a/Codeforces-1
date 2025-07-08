import sys

def solve():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        ob =[ ]
        for x in range(len(b)):
            if a[x]>b[x]:
                a[x],b[x] = b[x],a[x]
                ob.append([3,x+1])
        def min_adjacent_swaps_to_sort(arr,t):
                n = len(arr)
                swaps = 0
                a = arr[:]

                for i in range(n):
                    for j in range(n - 1):
                        if a[j] > a[j + 1]:
                            a[j], a[j + 1] = a[j + 1], a[j]
                            ob.append([t,j+1])
                            swaps += 1

                return swaps
        min_adjacent_swaps_to_sort(a,1)
        min_adjacent_swaps_to_sort(b,2)
        print(len(ob))
        for x in ob:
            print(*x)
if __name__ == '__main__':
    solve()