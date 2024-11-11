from math import floor

a, b, c = map(float, input().split())
D = b ** 2 - 4 * a * c

if D < 0:
    print('No roots')
elif D == 0:
    print('One root:', floor(-b / (2 * a)))
else:
    x1 = floor((-b + D ** 0.5) / (2 * a))
    x2 = floor((-b - D ** 0.5) / (2 * a))
    print('Two roots:', min(x1, x2), max(x1, x2))
