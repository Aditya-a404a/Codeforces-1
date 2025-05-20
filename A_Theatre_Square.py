n,m,a = list(map(int,input().split()))
def check(n, m, a):
    
    tiles_in_length = (n + a - 1) // a
    tiles_in_width = (m + a - 1) // a
    
   
    total_tiles = tiles_in_length * tiles_in_width
    
    return total_tiles
print(check(n, m, a))