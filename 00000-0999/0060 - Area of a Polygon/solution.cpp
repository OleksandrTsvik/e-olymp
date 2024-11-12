#include <iomanip>
#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;

    int **coordinates = new int *[n];

    for (int i = 0; i < n; i++) {
        coordinates[i] = new int[2];
        cin >> coordinates[i][0] >> coordinates[i][1];
    }

    // Shoelace formula
    double result = 0;

    result += coordinates[n - 1][0] * coordinates[0][1];
    result -= coordinates[0][0] * coordinates[n - 1][1];

    for (int i = 0; i < n - 1; i++) {
        result += coordinates[i][0] * coordinates[i + 1][1];
        result -= coordinates[i + 1][0] * coordinates[i][1];
    }

    result = 0.5 * abs(result);

    cout << fixed << setprecision(3) << result << "\n";
}
