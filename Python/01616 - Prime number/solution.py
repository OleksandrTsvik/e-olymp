n = int(input())
count = 2
for i in range(2, round(n ** 0.5)):
    if n % i == 0:
        count += 1
        break
if count == 2:
    print('Yes')
else:
    print('No')
