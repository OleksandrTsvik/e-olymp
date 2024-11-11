n = int(input())

a = {}
result = []
m = [0, 3, 4, 2, 5, 1, 6]
pryf = []
count = 1
Run = False
swim = save = temp = 0
ost = n

for i in range(n):
    name, r = map(str, input().split())
    pryf.append(name)
    result.append(r)
    a[r] = name

z = list(map(str, input().split()))
result = sorted(result, key=float)

if not z[0] in pryf:
    print("Missing")
else:
    for i in range(n):
        if (i + 1) % 6 == 0 and a[result[i]] != z[0]:
            ost -= 6
            count += 1
            swim = -1
        swim += 1
        if ost == 7 or ost == 8:
            swim = 0
            count = n // 6
            temp = (count - 1) * 6
            if ost == 7:
                save = 4
            if ost == 8:
                save = 5
            for j in range(temp, n):
                if swim == save:
                    count += 1
                    swim = 0
                swim += 1
                if a[result[j]] == z[0]:
                    Run = True
                    print(count, m[swim])
                    break
            if Run:
                break
        if a[result[i]] == z[0]:
            print(count, m[swim])
            break
