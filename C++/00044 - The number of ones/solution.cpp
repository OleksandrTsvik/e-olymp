#include <iostream>

using namespace std;

int main() {
    std::ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    int *ones = new int[n + 1]{0};
    ones[1] = 1;

    for (int i = 2; i <= n; i++) {
        ones[i] = i;

        for (int j = 1; 2 * j < i; j++) {
            int count = ones[j] + ones[i - j];

            if (ones[i] > count) {
                ones[i] = count;
            }
        }

        for (int j = 2; j * j <= i; j++) {
            if (i % j != 0) {
                continue;
            }

            int count = ones[j] + ones[i / j];

            if (ones[i] > count) {
                ones[i] = count;
            }
        }
    }

    cout << ones[n];
}
