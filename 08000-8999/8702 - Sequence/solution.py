n = int(input())

Fibonacci = [0, 1, 2]
Zeckendorf = n
j = n - 1
number = [1]
i = 3

for i in range(3, n + 1):
    Fibonacci.append(Fibonacci[i - 1] + Fibonacci[i - 2])
    if Fibonacci[i] <= n:
        Zeckendorf = Fibonacci[i]
        j = i - 1
    else:
        break

while j != 0:
    if Fibonacci[j] + Zeckendorf <= n:
        Zeckendorf += Fibonacci[j]
        number.append(1)
    else:
        number.append(0)
    j -= 1

print(*number, sep='')
