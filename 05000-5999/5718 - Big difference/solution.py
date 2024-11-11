n = int(input())
a = []
max_i = min_i = 0


def DecToBin(d):
    while d != 0:
        a.append(d % 2)
        d //= 2


def BinToDec(b):
    dec = 0
    b.reverse()
    for i in range(len(b)):
        if b[i] == 1:
            dec += 2 ** i
    return dec


DecToBin(n)

a.sort()

min_i = BinToDec(a)
max_i = BinToDec(a)

print(max_i - min_i)
