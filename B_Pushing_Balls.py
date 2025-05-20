import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        grid = [input().strip() for _ in range(n)]
        # vis[i][j] will be True if cell (i,j) is “covered” by
        # the leading-1’s in its row or column
        vis = [[False]*m for _ in range(n)]

        # Mark all leading 1’s in each row
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '0':
                    break
                vis[i][j] = True

        # Mark all leading 1’s in each column
        for j in range(m):
            for i in range(n):
                if grid[i][j] == '0':
                    break
                vis[i][j] = True

        # Check: every 1 must have been marked
        ok = True
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not vis[i][j]:
                    ok = False
                    break
            if not ok:
                break

        print("YES" if ok else "NO")

if __name__ == "__main__":
    solve()
