import sys
import math


def compute_circumcenter(x1, y1, x2, y2, x3, y3):
    # Using determinant formula
    d = 2 * (x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
    if abs(d) < 1e-12:
        return None  # Points are collinear or too close
    ux = ((x1*x1 + y1*y1)*(y2 - y3) + (x2*x2 + y2*y2)*(y3 - y1) + (x3*x3 + y3*y3)*(y1 - y2)) / d
    uy = ((x1*x1 + y1*y1)*(x3 - x2) + (x2*x2 + y2*y2)*(x1 - x3) + (x3*x3 + y3*y3)*(x2 - x1)) / d
    return ux, uy


def main():
    data = sys.stdin.read().strip().split()
    coords = list(map(float, data))
    x1, y1, x2, y2, x3, y3 = coords

    center = compute_circumcenter(x1, y1, x2, y2, x3, y3)
    if center is None:
        print("0.000000")
        return
    cx, cy = center
    # Radius
    R = math.hypot(x1 - cx, y1 - cy)

    # Angles of points
    angles = []
    for x, y in [(x1, y1), (x2, y2), (x3, y3)]:
        theta = math.atan2(y - cy, x - cx)
        if theta < 0:
            theta += 2 * math.pi
        angles.append(theta)
    angles.sort()

    # Arc lengths between consecutive points
    d1 = angles[1] - angles[0]
    d2 = angles[2] - angles[1]
    d3 = 2*math.pi - (angles[2] - angles[0])
    diffs = [d1, d2, d3]

    # Find minimal n such that each diff*n/(2pi) is integer
    eps = 1e-6
    best_n = None
    for n in range(3, 101):
        ok = True
        for d in diffs:
            x = d * n / (2 * math.pi)
            if abs(x - round(x)) > eps:
                ok = False
                break
        if ok:
            best_n = n
            break

    if best_n is None:
        best_n = 100

    # Compute area of regular polygon with n sides and radius R
    area = 0.5 * best_n * R * R * math.sin(2 * math.pi / best_n)
    print(f"{area:.6f}")

if __name__ == '__main__':
    main()
