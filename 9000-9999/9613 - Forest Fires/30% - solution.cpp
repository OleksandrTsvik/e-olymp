#include <iostream>

using namespace std;

int n, m;
int a[150][150]{}, c[150][150]{};

void Time(int x, int y) {
  if ((0 <= x) and (x <= n) and (0 <= y) and (y <= m)) {
    if ((0 <= x - 1) and (x - 1 <= n) and (0 <= y + 1) and (y + 1 <= m)) {
      if (::c[x - 1][y + 1] > a[x - 1][y + 1] + ::c[x][y] || ::c[x - 1][y + 1] == 0) {
        ::c[x - 1][y + 1] = a[x - 1][y + 1] + ::c[x][y];
        Time(x - 1, y + 1);
      }
    }

    if ((0 <= x) and (x <= n) and (0 <= y + 1) and (y + 1 <= m)) {
      if (::c[x][y + 1] > a[x][y + 1] + ::c[x][y] || ::c[x][y + 1] == 0) {
        ::c[x][y + 1] = a[x][y + 1] + ::c[x][y];
        Time(x, y + 1);
      }
    }

    if ((0 <= x + 1) and (x + 1 <= n) and (0 <= y + 1) and (y + 1 <= m)) {
      if (::c[x + 1][y + 1] > a[x + 1][y + 1] + ::c[x][y] || ::c[x + 1][y + 1] == 0) {
        ::c[x + 1][y + 1] = a[x + 1][y + 1] + ::c[x][y];
        Time(x + 1, y + 1);
      }
    }

    if ((0 <= x - 1) and (x - 1 <= n) and (0 <= y) and (y <= m)) {
      if (::c[x - 1][y] > a[x - 1][y] + ::c[x][y] || ::c[x - 1][y] == 0) {
        ::c[x - 1][y] = a[x - 1][y] + ::c[x][y];
        Time(x - 1, y);
      }
    }

    if ((0 <= x + 1) and (x + 1 <= n) and (0 <= y) and (y <= m)) {
      if (::c[x + 1][y] > a[x + 1][y] + ::c[x][y] || ::c[x + 1][y] == 0) {
        ::c[x + 1][y] = a[x + 1][y] + ::c[x][y];
        Time(x + 1, y);
      }
    }

    if ((0 <= x - 1) and (x - 1 <= n) and (0 <= y - 1) and (y - 1 <= m)) {
      if (::c[x - 1][y - 1] > a[x - 1][y - 1] + ::c[x][y] || ::c[x - 1][y - 1] == 0) {
        ::c[x - 1][y - 1] = a[x - 1][y - 1] + ::c[x][y];
        Time(x - 1, y - 1);
      }
    }

    if ((0 <= x) and (x <= n) and (0 <= y - 1) and (y - 1 <= m)) {
      if (::c[x][y - 1] > a[x][y - 1] + ::c[x][y] || ::c[x][y - 1] == 0) {
        ::c[x][y - 1] = a[x][y - 1] + ::c[x][y];
        Time(x, y - 1);
      }
    }

    if ((0 <= x + 1) and (x + 1 <= n) and (0 <= y - 1) and (y - 1 <= m)) {
      if (::c[x + 1][y - 1] > a[x + 1][y - 1] + ::c[x][y] || ::c[x + 1][y - 1] == 0) {
        ::c[x + 1][y - 1] = a[x + 1][y - 1] + ::c[x][y];
        Time(x + 1, y - 1);
      }
    }
  }
}

int main() {
  int k, xxx, yyy, xx, yy;

  cin >> ::n >> ::m >> k >> xxx >> yyy;

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      cin >> ::a[i][j];
    }
  }

  n -= 1;
  m -= 1;

  for (int i = 0; i < k; i++) {
    cin >> xx >> yy;

    if (::c[xx - 1][yy - 1] == 0 || a[xx - 1][yy - 1] < ::c[xx - 1][yy - 1]) {
      ::c[xx - 1][yy - 1] = a[xx - 1][yy - 1];
    }

    Time(xx - 1, yy - 1);
  }

  cout << c[xxx - 1][yyy - 1] - a[xxx - 1][yyy - 1] << endl;

  return 0;
}