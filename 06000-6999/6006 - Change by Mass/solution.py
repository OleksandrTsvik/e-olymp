ITEM_TYPE_COUNT = 5

values = [50, 25, 10, 5, 1]
weights = [11340, 5670, 2268, 5000, 2500]
counts = [float('inf')] * ITEM_TYPE_COUNT

request_number = 0

while True:
    request = input().split()
    cents = int(request[0])

    if cents == -1:
        break

    request_number += 1

    halfDollarCoinCount = int(request[1])
    counts[0] = halfDollarCoinCount

    # (weight, count)
    matrix = [[(float('inf'), float('inf'))] * (cents + 1) for _ in range(ITEM_TYPE_COUNT + 1)]
    matrix[0][0] = (0, 0)

    for i in range(1, ITEM_TYPE_COUNT + 1):
        itemIndex = i - 1

        for j in range(0, cents + 1):
            matrix[i][j] = matrix[i - 1][j]

            if counts[itemIndex] == float('inf'):
                if j >= values[itemIndex]:
                    new_weight, new_count = matrix[i][j - values[itemIndex]]

                    new_weight += weights[itemIndex]
                    new_count += 1

                    matrix[i][j] = min(matrix[i][j], (new_weight, new_count))
            else:
                count = min(int(counts[itemIndex]), j // values[itemIndex]) + 1

                for k in range(1, count):
                    if j >= values[itemIndex] * k:
                        new_weight, new_count = matrix[i - 1][j - values[itemIndex] * k]

                        new_weight += weights[itemIndex] * k
                        new_count += k

                        matrix[i][j] = min(matrix[i][j], (new_weight, new_count))

    current_value = cents
    used_counts = [0] * ITEM_TYPE_COUNT

    for i in range(ITEM_TYPE_COUNT, 0, -1):
        if current_value <= 0:
            break

        used = 0

        while current_value >= values[i - 1] * used and used <= counts[i - 1]:
            previous_value = current_value - values[i - 1] * used
            weight = matrix[i - 1][previous_value][0] + weights[i - 1] * used
            count = matrix[i - 1][previous_value][1] + used

            if matrix[i][current_value] == (weight, count):
                used_counts[i - 1] = used
                current_value = previous_value
                break

            used += 1

    response = f'Request {request_number}:'

    for i in range(ITEM_TYPE_COUNT):
        if used_counts[i] > 0:
            response += f' {used_counts[i]}x{values[i]}'

    print(response)
