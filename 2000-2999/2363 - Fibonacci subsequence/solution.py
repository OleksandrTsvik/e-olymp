n = int(input())
arr = list(map(int, input().split()))

arr.sort()
flag = True

for i in range(2, n):
    if not arr[i] == arr[i - 1] + arr[i - 2]:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")
