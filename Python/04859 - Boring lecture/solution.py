word = input()

length = len(word)
count_letters = {}

for letter in word:
    count_letters[letter] = 0

index = length

for i in range(int(length / 2)):
    count_letters[word[i]] += index
    count_letters[word[-i - 1]] += index

    index += length - (2 * i + 2)

if length % 2 == 1:
    count_letters[word[int(length / 2)]] += index

sorted_tuple = sorted(count_letters.items(), key=lambda x: x[0])

for letter in sorted_tuple:
    print(f"{letter[0]}: {letter[1]}")
