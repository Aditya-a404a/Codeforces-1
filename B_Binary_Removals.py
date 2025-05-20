T = int(input())
def check(s):
    from functools import lru_cache

    @lru_cache(None)
    def dp(index, can_remove, prev_char):
        if index == len(s):
            return True
        
        res = False
        
        # Option 1: Keep current character
        if int(prev_char) <= int(s[index]):
            
            res |= dp(index + 1, True, s[index])

        # Option 2: Remove current character if allowed
        if can_remove:
           
            res |= dp(index + 1, False, prev_char)

        return res

    return dp(0, True, '0')  # or use '?' or '' for prev_char initially



for _ in range(T):
    
    a = input()
    print("YES" if check(a) else "NO")
