s = input()
s = list(s)

while ' ' in s:
    s.remove(' ')

ss = s.copy()
s.reverse()

if s == ss:
    print('YES')
else:
    print('NO')
