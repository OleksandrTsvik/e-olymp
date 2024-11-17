test_case_count = int(input())
indexes = [int(input()) - 1 for i in range(test_case_count)]

new_fibonacci = [1, 1, 1, 1]
max_index = max(indexes)

for i in range(4, max_index + 1):
    new_fibonacci.append(new_fibonacci[i - 1] + new_fibonacci[i - 2] + new_fibonacci[i - 3] + new_fibonacci[i - 4])

for index in indexes:
    print(new_fibonacci[index])
