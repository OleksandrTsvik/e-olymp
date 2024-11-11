n = 1

while True and n != 0:
    n = int(input())
    t = n
    k = n * 2
    for i in range(1, n + 1):
        t -= 1
        print(' ' * t, '*' * (i * 2 - 1), ' ' * t, sep='')
    for i in range(1, n):
        t += 1
        k -= 2
        print(' ' * t, '*' * (k - 1), ' ' * t, sep='')
    print()
