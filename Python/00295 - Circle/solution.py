n = int(input())

count = 0
sqrN = n ** 2

for i in range(-n, n + 1):
    for j in range(1, n + 1):
        if i ** 2 + j ** 2 <= sqrN:
            count += 1
count *= 2
count += 2 * n + 1
print(count)
