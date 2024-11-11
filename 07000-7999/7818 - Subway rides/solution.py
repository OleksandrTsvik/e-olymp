m = int(input())
suma = 0

while m != 0:
    if m > 73:
        suma += m // 100 * 200
        if m <= 100:
            suma += 200
            m = 0
        else:
            m = m % 100
    elif 41 < m <= 73:
        suma += m // 50 * 125
        if m < 50:
            suma += 125
            m = 0
        else:
            m = m % 50
    elif 7 < m <= 41:
        suma += m // 10 * 30
        if m <= 10:
            suma += 30
            m = 0
        else:
            m = m % 10
    elif m <= 7:
        suma += m * 4
        m = 0

print(suma)
