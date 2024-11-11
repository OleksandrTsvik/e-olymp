n = int(input())
lst = list(map(float, input().split()))
count = suma = 0

for i in range(2, n, 3):
    if lst[i] > 0:
        count += 1
        suma += lst[i]
        
print(count, '{0:.2f}'.format(suma))
