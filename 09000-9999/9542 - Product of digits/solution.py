from math import ceil


def Prost(n):
    for i in range(2, ceil(n ** 0.5)):
        if n % i == 0:
            return False
    return True


m = int(input())
a = []

if m % 11 == 0:
    print(-1)
elif Prost(m) and m > 9:
    print(-1)
else:
    while m != 0:
        if m % 2 == 0:
            a.append(2)
            m = m // 2
        elif m % 3 == 0:
            a.append(3)
            m = m // 3
        elif m % 5 == 0:
            a.append(5)
            m = m // 5
        elif m % 7 == 0:
            a.append(7)
            m = m // 7
        else:
            m = 0
            a = sorted(a, key=int, reverse=True)
            print(*a, sep='')
