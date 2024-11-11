n = int(input())

count = 0
input()

for i in range(1, n):
    a = input()[:2 * i - 1].split(' ')
    for j in range(i):
        if a[j] == '1':
            count += 1

print(count)
