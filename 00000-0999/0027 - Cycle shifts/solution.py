n = int(input())
a = []
maxi = temp = suma = 0

while n != 0:
    if n % 2 == 1:
        a.append(1)
    else:
        a.append(0)
    n = n // 2

n = len(a)

for i in range(n):
    temp = a[0]

    for j in range(1, n):
        a[j - 1] = a[j]

    a[n - 1] = temp

    for l in range(n):
        suma += a[l] * 2 ** l

    if maxi < suma:
        maxi = suma

    suma = 0

print(maxi)
