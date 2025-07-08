T = int(input())

for _ in range(T):
    k, a_req, b_req, x_drop, y_drop = map(int, input().split())
    # ensure (a_req, x_drop) is the “gentler” (smaller drop) skewer
    if x_drop > y_drop:
        a_req, b_req, x_drop, y_drop = b_req, a_req, y_drop, x_drop

    # how many of type‑A can we cook?
    if k >= a_req:
        cntA = (k - a_req) // x_drop + 1
    else:
        cntA = 0
    k -= cntA * x_drop

    # how many of type‑B next?
    if k >= b_req:
        cntB = (k - b_req) // y_drop + 1
    else:
        cntB = 0

    print(cntA + cntB)




    



