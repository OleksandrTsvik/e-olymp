n, m, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)
count = 0
i = 0

while n >= k and i <= n - k:
    suma = 0
    for j in range(i, i + k - 1):
        suma += a[j] - a[j + 1]
    if suma < m:
        a.remove(min(a[i:i + k]))
        n -= 1
        count += 1
    else:
        i += 1

print(count)
