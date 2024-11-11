n, m, k, xxx, yyy = map(int, input().split())

a = []
c = [[0] * m for i in range(n)]

for i in range(n):
    a.append(list(map(int, input().split())))

n -= 1
m -= 1


def Time(x, y):
    global m, n, c, a
    if 0 <= x <= n and 0 <= y <= m:
        if 0 <= x - 1 <= n and 0 <= y + 1 <= m:
            if c[x - 1][y + 1] > a[x - 1][y + 1] + c[x][y] or c[x - 1][y + 1] == 0:
                c[x - 1][y + 1] = a[x - 1][y + 1] + c[x][y]
                Time(x - 1, y + 1)
        if 0 <= x <= n and 0 <= y + 1 <= m:
            if c[x][y + 1] > a[x][y + 1] + c[x][y] or c[x][y + 1] == 0:
                c[x][y + 1] = a[x][y + 1] + c[x][y]
                Time(x, y + 1)
        if 0 <= x + 1 <= n and 0 <= y + 1 <= m:
            if c[x + 1][y + 1] > a[x + 1][y + 1] + c[x][y] or c[x + 1][y + 1] == 0:
                c[x + 1][y + 1] = a[x + 1][y + 1] + c[x][y]
                Time(x + 1, y + 1)
        if 0 <= x - 1 <= n and 0 <= y <= m:
            if c[x - 1][y] > a[x - 1][y] + c[x][y] or c[x - 1][y] == 0:
                c[x - 1][y] = a[x - 1][y] + c[x][y]
                Time(x - 1, y)
        if 0 <= x + 1 <= n and 0 <= y <= m:
            if c[x + 1][y] > a[x + 1][y] + c[x][y] or c[x + 1][y] == 0:
                c[x + 1][y] = a[x + 1][y] + c[x][y]
                Time(x + 1, y)
        if 0 <= x - 1 <= n and 0 <= y - 1 <= m:
            if c[x - 1][y - 1] > a[x - 1][y - 1] + c[x][y] or c[x - 1][y - 1] == 0:
                c[x - 1][y - 1] = a[x - 1][y - 1] + c[x][y]
                Time(x - 1, y - 1)
        if 0 <= x <= n and 0 <= y - 1 <= m:
            if c[x][y - 1] > a[x][y - 1] + c[x][y] or c[x][y - 1] == 0:
                c[x][y - 1] = a[x][y - 1] + c[x][y]
                Time(x, y - 1)
        if 0 <= x + 1 <= n and 0 <= y - 1 <= m:
            if c[x + 1][y - 1] > a[x + 1][y - 1] + c[x][y] or c[x + 1][y - 1] == 0:
                c[x + 1][y - 1] = a[x + 1][y - 1] + c[x][y]
                Time(x + 1, y - 1)


for i in range(k):
    xx, yy = map(int, input().split())
    if c[xx - 1][yy - 1] == 0 or a[xx - 1][yy - 1] < c[xx - 1][yy - 1]:
        c[xx - 1][yy - 1] = a[xx - 1][yy - 1]
    Time(xx - 1, yy - 1)

print(c[xxx - 1][yyy - 1] - a[xxx - 1][yyy - 1])
