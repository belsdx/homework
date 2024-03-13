
def do_lines_intersect(p1, q1, p2, q2):
    def ccw(A, B, C):
        return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])
    return ccw(p1, q1, p2) != ccw(p1, q1, q2) and ccw(p2, q2, p1) != ccw(p2, q2, q1)


def is_self_intersecting(polygon):
    n = len(polygon)
    for i in range(n):
        for j in range(i+1, n):
            if i == j: continue
            line1 = (polygon[i], polygon[(i + 1) % n])
            line2 = (polygon[j], polygon[(j + 1) % n])
            if do_lines_intersect(*line1, *line2):
                return True
    return False


def is_convex(polygon):
    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    
    positive = negative = False
    n = len(polygon)
    for i in range(n):
        o, a, b = polygon[i], polygon[(i + 1) % n], polygon[(i + 2) % n]
        cp = cross_product(o, a, b)
        if cp > 0:
            positive = True
        elif cp < 0:
            negative = True
        if positive and negative:
            return False  
    return True  


polygon = [(5, -5), (2, 4), (-1, 1), (-2, 5), (-4, -5)]


print("多边形是否自相交：", is_self_intersecting(polygon))


print("多边形是否是凸的：", is_convex(polygon))


def is_point_inside_polygon(point, polygon):
    def on_segment(p, q, r):
        return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
                q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))

    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0: return 0
        return 1 if val > 0 else 2

    def do_intersect(p1, q1, p2, q2):
        o1 = orientation(p1, q1, p2)
        o2 = orientation(p1, q1, q2)
        o3 = orientation(p2, q2, p1)
        o4 = orientation(p2, q2, q1)
        return (o1 != o2 and o3 != o4) or \
            (o1 == 0 and on_segment(p1, p2, q1)) or \
            (o2 == 0 and on_segment(p1, q2, q1)) or \
            (o3 == 0 and on_segment(p2, p1, q2)) or \
            (o4 == 0 and on_segment(p2, q1, q2))

    INF = 10000
    ext_point = (INF, point[1])
    count = i = 0
    while True:
        next = (i + 1) % len(polygon)
        if do_intersect(polygon[i], polygon[next], point, ext_point):
            if orientation(polygon[i], point, polygon[next]) == 0:
                return on_segment(polygon[i], point, polygon[next])
            count += 1
        i = next
        if i == 0:
            break
    return count % 2 == 1



polygon = [(3, 1), (1, 3), (-1, 1), (-2, -3), (1, -4), (3, -2)]


points = [(1, -1), (-1, 2)]


for point in points:
    print(f"点 {point} {'在多边形内部' if is_point_inside_polygon(point, polygon) else '在多边形外部'}。")
