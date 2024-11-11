line = input()

for char in line:
    if (char.isalnum()):
        print(char, char, sep='', end='')
    else:
        print(char, sep='', end='')

print()
