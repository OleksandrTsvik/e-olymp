def tridiagonal_matrix_algorithm(a, b, c, d):
    n = len(b)
    x = [0.0] * n

    for i in range(1, n):
        coefficient = a[i] / b[i - 1]
        b[i] -= coefficient * c[i - 1]
        d[i] -= coefficient * d[i - 1]

    for i in range(n - 2, -1, -1):
        coefficient = c[i] / b[i + 1]
        d[i] -= coefficient * d[i + 1]

    for i in range(n):
        x[i] = d[i] / b[i]

    return x


count, first_weigth, last_weigth, watermelon_number = map(float, input().split())

count = int(count)
watermelon_index = int(watermelon_number) - 1

# consecutive tridiagonal matrix algorithm
main_diagonal = [0.0] * count
upper_diagonal = [0.0] * count
lower_diagonal = [0.0] * count
constant_column = [0.0] * count

main_diagonal[0] = 1
main_diagonal[count - 1] = 1

constant_column[0] = first_weigth
constant_column[count - 1] = last_weigth

for i in range(1, count - 1):
    lower_diagonal[i] = -1
    main_diagonal[i] = 2
    upper_diagonal[i] = -1
    constant_column[i] = -0.2

x = tridiagonal_matrix_algorithm(lower_diagonal, main_diagonal, upper_diagonal, constant_column)

if min(x) <= 0:
    print(-1)
else:
    print('{0:.3f}'.format(x[watermelon_index]))
