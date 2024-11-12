#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    unsigned long m, n;

    cin >> m >> n;

    if (m == 1 || n == 1) {
        cout << 1;
    } else {
        cout << (m - 1) * (n - 1) + 1;
    }
}
