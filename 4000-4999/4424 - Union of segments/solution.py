n = int(input())

arr = []

for i in range(n):
    l, r = map(int, input().split())
    arr.append([l, r])

arr.sort()
m = arr[0][1]

arrResult = [arr[0]]

for i in range(1, n):
    if arr[i][0] <= m and arr[i][1] > m:
        if arrResult[len(arrResult) - 1][1] < arr[i][1]:
            arrResult[len(arrResult) - 1][1] = arr[i][1]
    elif arr[i][0] > m:
        arrResult.append(arr[i])

    if m < arr[i][1]:
        m = arr[i][1]

print(len(arrResult))
for i in range(len(arrResult)):
    print(*arrResult[i])
