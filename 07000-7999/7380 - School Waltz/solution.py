n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort(reverse=True)

i = j = count = 0
c = [True] * max(n, m)

while i < n:
    while j < m:
        if a[i] >= b[j] and c[j]:
            count += 1
            c[j] = False
            break
        else:
            j += 1
    j = 0
    i += 1

print(count)
