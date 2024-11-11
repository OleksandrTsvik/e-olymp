def ConversionSecond(h, m, s):
    return h * 3600 + m * 60 + s


def AddZero(x):
    if x < 10:
        return '0' + str(x)
    return x


def ConversionTime(s):
    h = s // 3600
    s -= 3600 * h
    m = s // 60
    s -= 60 * m
    return h, m, s


t1, t2 = map(str, input().split())
h1, m1, s1 = t1.split(':')
h2, m2, s2 = t2.split(':')
if int(h2) < int(h1):
    h2 = int(h2) + 24
s1 = ConversionSecond(int(h1), int(m1), int(s1))
s2 = ConversionSecond(int(h2), int(m2), int(s2))
s = s2 - s1
h, m, s = ConversionTime(s)
print(AddZero(h), AddZero(m), AddZero(s), sep=':')
