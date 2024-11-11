n = int(input())

A = 2
B = 1
d = 1

while d != n:
    d = d * B

    if d > n:
        A += 1
        d = A
        B = A + 1
    elif d == n:
        print(A, B)
    else:
        B = B + 1
