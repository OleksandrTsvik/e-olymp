a, b = map(str, input().split('+'))

numbers = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'VIII': 8,
    'VII': 7,
    'VI': 6,
    'V': 5,
    'IV': 4,
    'I': 1
}

roman = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    8: 'VIII',
    7: 'VII',
    6: 'VI',
    5: 'V',
    4: 'IV',
    1: 'I'
}

n = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 8, 7, 6, 5, 4, 1]

numA = 0
numB = 0


def Numeric(x, num):
    t = 'M'
    for i in x:
        if numbers[i] > numbers[t]:
            num -= numbers[t]
            num += numbers[i] - numbers[t]
        else:
            num += numbers[i]
        t = i
    return num


def Answer(num):
    answer = ''
    for i in range(len(n)):
        if num >= n[i]:
            answer += roman[n[i]] * (num // n[i])
            num -= n[i] * (num // n[i])
    return answer


numA = Numeric(a, numA)
numB = Numeric(b, numB)

print(Answer(numA + numB))
