#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    long arraySize, requestCount;
    cin >> arraySize >> requestCount;

    arraySize++;
    long *array = new long[arraySize]{0};
    long *sums = new long[arraySize]{0};

    char requestType;
    long a, b;

    for (long i = 0; i < requestCount; i++) {
        cin >> requestType >> a >> b;

        if (requestType == 'A') {
            array[a] = b;

            for (long j = a; j < arraySize; j++) {
                sums[j] = sums[j - 1] + array[j];
            }
        } else {
            cout << sums[b] - sums[a - 1] << "\n";
        }
    }
}
