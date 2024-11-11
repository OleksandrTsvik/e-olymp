n = int(input())
m = [0] + list(map(int, input().split()))
c = [0] + list(map(int, input().split()))

l = len(m)

a = [[[0, set([])] for j in range(n + 1)] for i in range(l)]

for i in range(1, l):
    for j in range(n + 1):
        a[i][j][0] = a[i - 1][j][0]
        a[i][j][1].update(a[i - 1][j][1])

        if j - m[i] >= 0:
            if a[i][j][0] < a[i - 1][j - m[i]][0] + c[i]:
                a[i][j][1].clear()
                a[i][j][1].add(i)
                a[i][j][1].update(a[i - 1][j - m[i]][1])

            a[i][j][0] = max(a[i][j][0], a[i - 1][j - m[i]][0] + c[i])

maxx = 0
index = 0

for i in range(1, n + 1):
    if maxx < a[l - 1][i][0]:
        maxx = a[l - 1][i][0]
        index = i

print(*a[l - 1][index][1], sep='\n')
