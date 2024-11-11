#include <iostream>

using namespace std;

int main() {
    std::ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    unsigned long segmentLength;
    cin >> segmentLength;

    // Three segments can make a triangle if and only if the sum of the lengths
    // of the shorter segments is greater than the length of the longer one.
    unsigned long invalidTrianglePartCount = 0;

    // 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ..., a[i - 2] + a[i - 1]
    unsigned long fibonacciNumber = 1;
    unsigned long nextFibonacciNumber = 1;

    while (segmentLength >= fibonacciNumber) {
        segmentLength -= fibonacciNumber;
        invalidTrianglePartCount++;

        unsigned long fibonacciSum = fibonacciNumber + nextFibonacciNumber;
        fibonacciNumber = nextFibonacciNumber;
        nextFibonacciNumber = fibonacciSum;
    }

    cout << invalidTrianglePartCount;
}
