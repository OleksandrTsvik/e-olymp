n = int(input())

n = list(str(n))
n.sort(key=int)

print((int(''.join(n)) - int(''.join(reversed(n)))) ** 2)
