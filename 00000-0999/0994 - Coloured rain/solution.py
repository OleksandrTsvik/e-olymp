n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
input()
b = list(map(int, input().split()))

count = 0

for i in range(n):
    for j in range(i):
        if a[i][j] and b[i] != b[j]:
            count += 1

print(count)
