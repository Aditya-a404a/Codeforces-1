def find_min_max(m, s):
    # 1) Impossibility
    if s == 0:
        return ("0", "0") if m == 1 else ("-1", "-1")
    if s > 9 * m:
        return ("-1", "-1")

    # 2) Build max (left→right greedy)
    rem = s
    max_digits = []
    for _ in range(m):
        d = min(9, rem)
        max_digits.append(str(d))
        rem -= d
    max_num = "".join(max_digits)

    # 3) Build min (left→right greedy with feasibility check)
    rem = s
    min_digits = []
    for pos in range(m):
        slots_left = m - pos - 1
        # lower bound: avoid leading zero, and leave enough capacity for the rest
        lo = rem - 9 * slots_left
        if pos == 0:
            lo = max(lo, 1)
        else:
            lo = max(lo, 0)
        # pick the smallest feasible digit
        d = lo
        min_digits.append(str(d))
        rem -= d

    min_num = "".join(min_digits)
    return (min_num, max_num)


if __name__ == "__main__":
    m, s = map(int, input().split())
    mn, mx = find_min_max(m, s)
    print(mn, mx)

        
        

    
