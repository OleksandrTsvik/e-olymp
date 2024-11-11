a, b, x = map(int, input().split())

time = jump = 0
t = a + b
Run = True

while jump != x:
    if (x > 0 and t > 0 and (jump + a + b <= x or jump + a <= x)) or (
        x < 0 and t < 0 and (jump + a + b >= x or jump + a >= x)):
        jump += a
        time += abs(a)

        if jump == x:
            Run = False
            print(time)
            break
        else:
            jump += b
            time += abs(b)
    else:
        Run = False
        print(-1)
        break

if Run:
    print(time)
