n = int(input())

if n == 1:
    print(10, 0)
    exit()

# search for digits that can be used to make an equal sum and product for an n-digit number
digits = set()
first_number = -1
start = int('1' * n)
stop = start + 888

for number in range(start, stop):
    number_str = str(number)

    if '0' in number_str:
        continue

    res_sum = 0
    res_product = 1

    for d in number_str:
        digit = int(d)
        res_sum += digit
        res_product *= digit

    if res_sum == res_product:
        digits.update(map(int, number_str))

        if first_number == -1:
            first_number = number

# calculate sums and products for different combinations of digits
digits = list(digits)
dp_prev = []
dp_next = []

for digit in digits:
    dp_next.append((digit, digit))

for i in range(1, n - 1):
    dp_prev = dp_next
    dp_next = []

    for digit in digits:
        for j in range(len(dp_prev)):
            prev_sum, prev_product = dp_prev[j]

            new_sum = prev_sum + digit
            new_product = prev_product * digit

            dp_next.append((new_sum, new_product))

count = 0

for digit in digits:
    for j in range(len(dp_next)):
        prev_sum, prev_product = dp_next[j]

        new_sum = prev_sum + digit
        new_product = prev_product * digit

        if new_sum == new_product:
            count += 1

print(count, first_number)
