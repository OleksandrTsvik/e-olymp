#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>

using namespace std;

bool inPolygon(long *polygon_x, long *polygon_y, long x, long y, long n);

int main() {
    std::ios::sync_with_stdio(false);

    long count = 0;
    long n, m, k;

    cin >> n >> m >> k;

    long *polygon_points_x = new long[n];
    long *polygon_points_y = new long[n];

    for (long i = 0; i != n; i++) {
        cin >> polygon_points_x[i] >> polygon_points_y[i];
    }

    for (long i = 0; i != m; i++) {
        long x, y;
        cin >> x >> y;

        if (count == k) {
            continue;
        }

        if (inPolygon(polygon_points_x, polygon_points_y, x, y, n)) {
            count++;
        }
    }

    if (count >= k) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
}

bool inPolygon(long *polygon_x, long *polygon_y, long x, long y, long n) {
    double summa = 0;

    for (long i = 0; i != n - 1; i++) {
        long va[] = {polygon_x[i] - x, polygon_y[i] - y};
        long vb[] = {polygon_x[i + 1] - x, polygon_y[i + 1] - y};

        long ab = va[0] * vb[0] + va[1] * vb[1];
        double a = sqrt(va[0] * va[0] + va[1] * va[1]);
        double b = sqrt(vb[0] * vb[0] + vb[1] * vb[1]);

        double mul = a * b;

        if (mul != 0) {
            summa += acos(ab / mul);
        } else {
            return true;
        }
    }

    long va[] = {polygon_x[n - 1] - x, polygon_y[n - 1] - y};
    long vb[] = {polygon_x[0] - x, polygon_y[0] - y};

    long ab = va[0] * vb[0] + va[1] * vb[1];
    double a = sqrt(va[0] * va[0] + va[1] * va[1]);
    double b = sqrt(vb[0] * vb[0] + vb[1] * vb[1]);

    double mul = a * b;

    if (mul != 0) {
        summa += acos(ab / mul);
    } else {
        return true;
    }

    return (2 * M_PI - 0.00001 < summa && summa < 2 * M_PI + 0.00001);
}