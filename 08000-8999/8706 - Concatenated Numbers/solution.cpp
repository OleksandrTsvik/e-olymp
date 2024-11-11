#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>
#include <sstream>
#include <string>

using namespace std;

int StrToInt(string line) {
    int number = 0;

    for (int i = 0; i < line.length(); i++) {
        int digit = int(line[i]) - (int)'0';
        number = number * 10 + digit;
    }

    return number;
}

string IntToStr(int number) {
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

int main() {
    bool Run;
    int n, num = 0, count = 0, i = 3, t, last, len;

    cin >> n;

    int *a = new int[300000]{2};
    int *arr = new int[1000000]{2};
    int *isNumber = new int[1000000]{};

    if (n < 5000) {
        t = round((3 * n) / 5) + 2;
    } else {
        t = round(n / 2);
    }

    while (count <= t) {
        Run = true;

        for (int j = 2; j <= round(sqrt(i)); j++) {
            if (i % j == 0) {
                Run = false;
                break;
            }
        }

        if (Run) {
            count += 1;
            a[count] = i;
            arr[count] = i;
            isNumber[i] = 1;
        }

        i += 2;
    }

    i = 0;
    len = count;
    last = a[count];

    while (StrToInt(IntToStr(a[i]) + IntToStr(a[0])) <= last) {
        for (int j = 0; j < len; j++) {
            num = StrToInt(IntToStr(a[i]) + IntToStr(a[j]));

            if (num > last) {
                break;
            } else if (isNumber[num] == 0) {
                count += 1;
                arr[count] = num;
                isNumber[num] = 1;
            }
        }

        i += 1;
    }

    vector<int> v(arr, arr + count);
    sort(v.begin(), v.end());

    cout << v[n - 1];

    return 0;
}