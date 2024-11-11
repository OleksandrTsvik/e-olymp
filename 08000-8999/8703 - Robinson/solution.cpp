#include <iostream>

using namespace std;

int n, m, a, b;
int distance[100][100]{}, arr[100][100]{};

int Length(int d, int nex) {
  if (nex == 1)
    return d + 1;
  else if (nex == 0)
    return d + 3;
}

void DistanceHome(int x, int y) {
  if (0 <= x <= n - 1 & 0 <= y <= m - 1) {
    if ((y >= 0 & y <= m - 1) & (y - 1 >= 0 & y - 1 <= m - 1)) {
      if (::distance[x][y - 1] == 0 || Length(::distance[x][y], arr[x][y - 1]) < ::distance[x][y - 1]) {
        ::distance[x][y - 1] = Length(::distance[x][y], arr[x][y - 1]);
        DistanceHome(x, y - 1);
      }
    }

    if ((y >= 0 & y <= m - 1) & (y + 1 >= 0 & y + 1 <= m - 1)) {
      if (::distance[x][y + 1] == 0 || Length(::distance[x][y], arr[x][y + 1]) < ::distance[x][y + 1]) {
        ::distance[x][y + 1] = Length(::distance[x][y], arr[x][y + 1]);
        DistanceHome(x, y + 1);
      }
    }

    if ((x >= 0 & x <= n - 1) & (x - 1 >= 0 & x - 1 <= n - 1)) {
      if (::distance[x - 1][y] == 0 || Length(::distance[x][y], arr[x - 1][y]) < ::distance[x - 1][y]) {
        ::distance[x - 1][y] = Length(::distance[x][y], arr[x - 1][y]);
        DistanceHome(x - 1, y);
      }
    }

    if ((x >= 0 & x <= n - 1) & (x + 1 >= 0 & x + 1 <= n - 1)) {
      if (::distance[x + 1][y] == 0 || Length(::distance[x][y], arr[x + 1][y]) < ::distance[x + 1][y]) {
        ::distance[x + 1][y] = Length(::distance[x][y], arr[x + 1][y]);
        DistanceHome(x + 1, y);
      }
    }
  }
}

int main() {
  cin >> ::n >> ::m >> ::a >> ::b;

  a -= 1;
  b -= 1;
  int minTime, c, d, south[m]{}, time[m]{};

  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++)
      cin >> ::arr[i][j];

  ::distance[a][b] = 1;

  DistanceHome(a, b);

  for (int i = 0; i < m; i++)
    for (int j = n - 1; j != -1; j--) {
      if (::arr[j][i] == 1) {
        south[i] = j + 1;
        time[i] = ::distance[j][i];
        minTime = time[i];
        break;
      }
    }

  for (int i = 0; i < m; i++) {
    if (minTime >= time[i] & time[i] != 0) {
      minTime = time[i];
      c = south[i];
      d = i + 1;
    }
  }

  cout << minTime << endl;
  cout << c << " " << d << endl;
}