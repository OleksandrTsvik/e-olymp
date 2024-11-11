s = list(input())
s.sort()

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        print('YES')
        break
else:
    print('NO')
