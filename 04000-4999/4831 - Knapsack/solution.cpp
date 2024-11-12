#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    const int MAX_WEIGHT_COUNT = 300;

    int knapsackCapacity;
    cin >> knapsackCapacity;

    int inputWeight;
    int weightCount = 0;
    int weights[MAX_WEIGHT_COUNT];

    while (cin >> inputWeight) {
        if (inputWeight > 0 && inputWeight <= knapsackCapacity) {
            weights[weightCount] = inputWeight;
            weightCount++;
        }
    }

    bool **matrix = new bool *[weightCount + 1];
    matrix[0] = new bool[knapsackCapacity + 1]{false};
    matrix[0][0] = true;

    for (int i = 1; i <= weightCount; i++) {
        int weightIndex = i - 1;
        matrix[i] = new bool[knapsackCapacity + 1]{false};

        for (int j = 0; j <= knapsackCapacity; j++) {
            matrix[i][j] = matrix[i - 1][j];

            if (weights[weightIndex] <= j && matrix[i - 1][j - weights[weightIndex]]) {
                matrix[i][j] = true;
            }
        }
    }

    for (int j = knapsackCapacity; j >= 0; j--) {
        if (matrix[weightCount][j]) {
            cout << j << "\n";
            break;
        }
    }
}
