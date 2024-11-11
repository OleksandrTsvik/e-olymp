n = int(input())
a = list(map(int, input().split()))

if a.count(3) <= 1 and 100 * (a.count(3) + a.count(4)) / n <= 25:
    print('Degree with honors')
else:
    print('Ordinary degree')
