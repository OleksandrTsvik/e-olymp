def Length(d, nex):
    if nex == 1:
        return d + 1
    elif nex == 0:
        return d + 3


def DistanceHome(x, y):
    global distance, n, m, arr
    if 0 <= x <= n - 1 and 0 <= y <= m - 1:
        if (y >= 0 and y <= m - 1) and (y - 1 >= 0 and y - 1 <= m - 1):
            if distance[x][y - 1] == 0 or Length(distance[x][y], arr[x][y - 1]) < distance[x][y - 1]:
                distance[x][y - 1] = Length(distance[x][y], arr[x][y - 1])
                DistanceHome(x, y - 1)
        if (y >= 0 and y <= m - 1) and (y + 1 >= 0 and y + 1 <= m - 1):
            if distance[x][y + 1] == 0 or Length(distance[x][y], arr[x][y + 1]) < distance[x][y + 1]:
                distance[x][y + 1] = Length(distance[x][y], arr[x][y + 1])
                DistanceHome(x, y + 1)
        if (x >= 0 and x <= n - 1) and (x - 1 >= 0 and x - 1 <= n - 1):
            if distance[x - 1][y] == 0 or Length(distance[x][y], arr[x - 1][y]) < distance[x - 1][y]:
                distance[x - 1][y] = Length(distance[x][y], arr[x - 1][y])
                DistanceHome(x - 1, y)
        if (x >= 0 and x <= n - 1) and (x + 1 >= 0 and x + 1 <= n - 1):
            if distance[x + 1][y] == 0 or Length(distance[x][y], arr[x + 1][y]) < distance[x + 1][y]:
                distance[x + 1][y] = Length(distance[x][y], arr[x + 1][y])
                DistanceHome(x + 1, y)


n, m, a, b = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

a -= 1
b -= 1

distance = [[0] * m for i in range(n)]

if arr[a][b] == 1:
    distance[a][b] = 1
elif arr[a][b] == 0:
    distance[a][b] = 3

DistanceHome(a, b)

south = [0] * m
time = [0] * m

for i in range(m):
    for j in range(n - 1, -1, -1):
        if arr[j][i] == 1:
            south[i] = j + 1
            time[i] = distance[j][i]
            minTime = time[i]
            break

for i in range(m):
    if minTime >= time[i] and time[i] != 0:
        minTime = time[i]
        c = south[i]
        d = i + 1

print(minTime)
print(c, d)
