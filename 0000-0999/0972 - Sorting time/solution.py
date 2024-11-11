n = int(input())
t = [list(map(int, input().split())) for i in range(n)]
t = sorted(t)

for i in range(n):
    print(*t[i], end='')
    print()
