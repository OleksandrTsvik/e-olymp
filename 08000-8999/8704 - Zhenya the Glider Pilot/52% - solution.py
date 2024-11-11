n, h = map(int, input().split())

x1 = [0] * n
x2 = [0] * n

for i in range(n):
    x1[i], x2[i] = map(int, input().split())

x1.sort()
x2.sort()

result = []

for i in range(n):
    height = h
    j = x1[i]
    k = i

    while height != 0:
        if j in x1:
            j += x2[x1.index(j)] - j
            k += 1
        elif k < n and height >= x1[k] - j:
            height -= abs(x1[k]) - abs(j)
            j += x1[k] - j
        else:
            j += height
            height = 0

    result.append(j - x1[i])

print(max(result))
