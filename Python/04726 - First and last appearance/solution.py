line = list(input())

if (line.count('f') == 1):
    print(line.index('f'))
elif (line.count('f') >= 2):
    for i in range(len(line) - 1, 0, -1):
        if (line[i] == 'f'):
            print(line.index('f'), i)
            break
