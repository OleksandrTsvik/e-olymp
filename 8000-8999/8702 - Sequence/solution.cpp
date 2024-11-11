#include <iostream>
#include <string>

using namespace std;

string IntToStr(unsigned long long number) {
    string line = "";
    int digit;
    char num = 0;

    while (number != 0) {
        digit = number % 10;
        number /= 10;
        num = (char)(digit + 48);
        line = num + line;
    }

    return line;
}

unsigned long long StrToInt(string line) {
    unsigned long long number = 0;

    for (unsigned long i = 0; i < line.length(); i++) {
        int digit = int(line[i]) - (int)'0';
        number = number * 10 + digit;
    }

    return number;
}

int main() {
    string new_element;
    unsigned long long n, s_element, count = 4, j;

    cin >> n;

    unsigned long long sequence[n]{1, 10, 100, 101};
    s_element = 100;

    while (count <= n) {
        j = 0;
        s_element *= 10;
        sequence[count] = s_element;
        new_element = IntToStr(s_element + sequence[j]);

        while (new_element[1] != '1' and count <= n) {
            j += 1;
            count += 1;
            sequence[count] = StrToInt(new_element);
            new_element = IntToStr(s_element + sequence[j]);
        }

        count += 1;
    }

    cout << sequence[n - 1];
}
