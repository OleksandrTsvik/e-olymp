from math import acos, sqrt, pi


def in_polygon(polygon, x, y):
    summa = 0

    for i in range(-1, len(polygon) - 1):
        va = [polygon[i][0] - x, polygon[i][1] - y]
        vb = [polygon[i + 1][0] - x, polygon[i + 1][1] - y]

        ab = va[0] * vb[0] + va[1] * vb[1]
        a = sqrt(va[0] * va[0] + va[1] * va[1])
        b = sqrt(vb[0] * vb[0] + vb[1] * vb[1])

        mul = a * b

        if mul != 0:
            summa += acos(ab / mul)
        else:
            return True

    return 2 * pi - 0.001 < summa < 2 * pi + 0.001


n, m, k = map(int, input().split())

polygon_points = []

for i in range(n):
    polygon_points.append(list(map(int, input().split())))

count = 0
for i in range(m):
    x, y = map(int, input().split())

    if count == k:
        continue

    if in_polygon(polygon_points, x, y):
        count += 1

if count == k:
    print('YES')
else:
    print('NO')
