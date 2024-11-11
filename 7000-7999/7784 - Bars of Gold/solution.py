x1, x2, x3 = map(int, input().split())

a = [x1, x2, x3]
k = a.index(max(a)) + 1
temp = 0
t = sum(a)
a = sorted(a)

if a[0] + a[1] == a[2]:
    print(0)
else:
    temp = t // 2 - a[0]
    a[2] -= temp
    if a[1] + a[2] == a[0] + temp:
        print(k)
        print(temp, a[2])
    else:
        print(-1)
