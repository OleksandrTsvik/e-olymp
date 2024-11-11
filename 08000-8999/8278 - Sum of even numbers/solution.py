a, b = map(int, input().split())
count = 0

if a < 0 < b and abs(a) > abs(b):
    b = -1 * b
    while a < b:
        if a % 2 == 0:
            count += a
        a += 1
    print(count)
elif a < 0 < b and abs(a) < abs(b):
    a = -1 * a + 1
    while a <= b:
        if a % 2 == 0:
            count += a
        a += 1
    print(count)
else:
    if a % 2 != 0 and a > 0:
        a += 1
    if a % 2 != 0 and a < 0:
        a += 1
    if b % 2 != 0 and b > 0:
        b -= 1
    if b % 2 != 0 and b < 0:
        b -= 1
    print('{0:.0f}'.format((a + b + 1) // 2 * (abs(abs(b) - abs(a)) + 2) // 2))
