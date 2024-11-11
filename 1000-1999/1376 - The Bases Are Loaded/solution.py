hex_to_decimal = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

decimal_to_hex = {
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '10': 'A',
    '11': 'B',
    '12': 'C',
    '13': 'D',
    '14': 'E',
    '15': 'F'
}


def DecToAny(base1, base2, number):
    if base2 == '10':
        return int(number, int(base1))

    dec = int(number, int(base1))
    result = []

    while dec != 0:
        result.append(decimal_to_hex[str(dec % int(base2))])
        dec //= int(base2)

    return ''.join(reversed(result))


try:
    while True:
        Run = True
        base1, base2, number = map(str, input().split())

        for i in number:
            if hex_to_decimal[i] > int(base1) - 1:
                Run = False

        if Run:
            print(number, 'base', base1, '=', DecToAny(base1, base2, number), 'base', base2)
        else:
            print(number, 'is an illegal base', base1, 'number')
except Exception:
    pass
