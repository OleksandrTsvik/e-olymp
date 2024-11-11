#include <iostream>
#include <string>
#include <map>

using namespace std;

int main() {
    std::ios::sync_with_stdio(false);

    string word;
    map<char, long> count_letters;

    getline(cin, word);

    long index = (int)word.length();

    for (int i = 0; i != (int)word.length() / 2; i++) {
        count_letters[word[i]] += index;
        count_letters[word[(int)word.length() - 1 - i]] += index;

        index += (int)word.length() - (2 * i + 2);
    }

    if ((int)word.length() % 2 == 1) {
        count_letters[word[(int)word.length() / 2]] += index;
    }

    map<char, long>::iterator it = count_letters.begin();

    for (; it != count_letters.end(); it++) {
        printf("%c: %li\n", it->first, it->second);
    }
}