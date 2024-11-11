n = int(input())

arr = []
length = 0

for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])

arr.sort()
length = arr[0][1] - arr[0][0]
m = arr[0][1]

for i in range(1, n):
    if arr[i][0] >= m:
        length += arr[i][1] - arr[i][0]
    elif arr[i][0] < m and arr[i][1] > m:
        length += arr[i][1] - m

    if m < arr[i][1]:
        m = arr[i][1]

print(length)
