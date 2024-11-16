#include <iostream>
#include <math.h>
#include <string>
#include <vector>

using namespace std;

int charToDigit(char c);

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    if (n == 1) {
        cout << 10 << " " << 0 << "\n";
        return 0;
    }

    vector<int> nDigitNumbers = {};
    unsigned int start = round(pow(10, n - 1));
    unsigned int stop = (n + 1) * round(pow(10, n - 1));

    for (int number = start; number < stop; number++) {
        string numberStr = to_string(number);

        if (numberStr.contains('0')) {
            continue;
        }

        int sum = 0;
        int product = 1;

        for (int j = 0; j < numberStr.length(); j++) {
            int digit = charToDigit(numberStr[j]);
            sum += digit;
            product *= digit;
        }

        if (sum == product) {
            nDigitNumbers.push_back(number);
        }
    }

    cout << nDigitNumbers.size() << " " << nDigitNumbers[0] << "\n";
}

int charToDigit(char c) {
    int number = c - '0';
    return number;
}
