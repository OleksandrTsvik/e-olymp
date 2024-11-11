#include <iostream>

using namespace std;

int main(void) {
  int n, min, max;

  cin >> n;
  int watermelons[n];

  for (int i = 0; i < n; i++) {
	cin >> watermelons[i];
  }

  if (n < 2) {
	cout << "Ooops!";
  } else {
	min = watermelons[0];
	max = watermelons[0];

	for (int i = 0; i < n; i++) {
	  if (max < watermelons[i])
		max = watermelons[i];
	  if (min > watermelons[i])
		min = watermelons[i];
	}

	cout << min << " " << max;
  }
}
