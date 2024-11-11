s = list(input().split())

k = 0
c = 0
char = 0

for j in range(5):
    for i in range(4):
        if int(s[i]) > int(s[i + 1]):
            temp = s[i + 1]
            s[i + 1] = s[i]
            s[i] = temp

if (int(s[0]) + 1 == int(s[1])) and (
        int(s[1]) + 1 == int(s[2])) and (
        int(s[2]) + 1 == int(s[3])) and (
        int(s[3]) + 1 == int(s[4])):
    print("Straight")
else:
    for i in range(14):
        if s.count(str(i)) == 1:
            char += 1
        if s.count(str(i)) == 5:
            print("Impossible")
            break
        elif s.count(str(i)) == 4:
            print("Four of a Kind")
            break
        elif s.count(str(i)) == 2:
            for j in range(14):
                if s.count(str(j)) == 3:
                    c = 1
                    print("Full House")
                    break
                elif s.count(str(j)) == 2:
                    k += 1
        elif s.count(str(i)) == 3 and c == 0 and ((s[3] != s[4]) or (s[0] != s[1])):
            print("Three of a Kind")
            break
        elif s.count(str(i)) == 3 and c == 0 and (s[3] == s[4]):
            print("Full House")
            break
        elif char == 5:
            print("Nothing")
            break

if k == 4 and c == 0:
    print("Two Pairs")
elif k == 1 and c == 0:
    print("One Pair")
