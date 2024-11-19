#include <iostream>
#include <math.h>

using namespace std;

int getTrailingZeros(int number);
int getDigitSum(unsigned long long number);

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int m;
    cin >> m;

    int nineCount = m / 9 + getTrailingZeros(m);
    unsigned long long result = m;

    if (nineCount > 1 && m % 9 != 0) {
        result = 9 + pow(10, nineCount);
    }

    for (int i = 1; i < nineCount; i++) {
        result += 9 * pow(10, i);
    }

    result -= result % m;
    int digitSum = getDigitSum(result);

    while (digitSum != m || result % m != 0) {
        result += m;
        digitSum = getDigitSum(result);

        if (m - digitSum >= 27) {
            result += pow(9, (m - digitSum) / 9);
            result -= result % m;
        }
    }

    cout << result << "\n";
}

int getTrailingZeros(int number) {
    int count = 0;

    while (number % 10 == 0) {
        number /= 10;
        count++;
    }

    return count;
}

int getDigitSum(unsigned long long number) {
    int sum = 0;

    while (number != 0) {
        sum += number % 10;
        number /= 10;
    }

    return sum;
}
