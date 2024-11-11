n, m = map(int, input().split())
a = [[0 for i in range(n)] for j in range(n)]

for i in range(m):
    j, k = map(int, input().split())
    a[j - 1][k - 1] = 1

b = [0 for i in range(n)]

for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            b[j] += 1
            b[i] += 1

if b.count(n - 1) == n:
    print('YES')
else:
    print('NO')
