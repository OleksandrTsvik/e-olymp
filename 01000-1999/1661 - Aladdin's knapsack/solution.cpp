#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int knapsackCapacity, itemTypeCount;
    cin >> knapsackCapacity >> itemTypeCount;

    int *weights = new int[itemTypeCount];
    int *costs = new int[itemTypeCount];

    for (int i = 0; i < itemTypeCount; i++) {
        cin >> weights[i] >> costs[i];
    }

    int **matrix = new int *[itemTypeCount + 1];
    matrix[0] = new int[knapsackCapacity + 1]{0};

    for (int i = 1; i <= itemTypeCount; i++) {
        int itemIndex = i - 1;
        matrix[i] = new int[knapsackCapacity + 1]{0};

        for (int j = 0; j <= knapsackCapacity; j++) {
            matrix[i][j] = matrix[i - 1][j];

            if (j >= weights[itemIndex]) {
                matrix[i][j] = max(matrix[i][j], matrix[i][j - weights[itemIndex]] + costs[itemIndex]);
            }
        }
    }

    cout << matrix[itemTypeCount][knapsackCapacity] << "\n";
}
