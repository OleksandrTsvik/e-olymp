char_En = ord('a')
CHAR_En = ord('A')

CHARS_En = [chr(CHAR_En + i) for i in range(26)]
chars_En = [chr(char_En + i) for i in range(26)]

c = input()

if (c == 'A'):
    print(CHARS_En[1])
elif (c == 'a'):
    print(chars_En[1])
elif (c == 'Z'):
    print(CHARS_En[len(CHARS_En) - 2])
elif (c == 'z'):
    print(chars_En[len(chars_En) - 2])
elif (c in CHARS_En):
    print(CHARS_En[CHARS_En.index(c) - 1], CHARS_En[CHARS_En.index(c) + 1])
elif (c in chars_En):
    print(chars_En[chars_En.index(c) - 1], chars_En[chars_En.index(c) + 1])
