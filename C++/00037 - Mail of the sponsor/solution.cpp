#include <iostream>
#include <set>

using namespace std;

void dfs(set<long> graph[], long startVertex, bool visited[]);

int main() {
    std::ios::sync_with_stdio(false);

    long n, s, k;
    cin >> n >> s >> k;

    set<long> *graph = new set<long>[ n ];

    for (long i = 0; i < k; i++) {
        long a, b;
        cin >> a >> b;

        graph[a - 1].insert(b - 1);
        graph[b - 1].insert(a - 1);
    }

    bool *visitedVertices = new bool[n]{false};
    int minNewConnectionCount = 0;

    dfs(graph, s - 1, visitedVertices);

    for (long i = 0; i < n; i++) {
        if (visitedVertices[i]) {
            continue;
        }

        minNewConnectionCount++;
        dfs(graph, i, visitedVertices);
    }

    cout << minNewConnectionCount;
}

void dfs(set<long> graph[], long startVertex, bool visited[]) {
    if (visited[startVertex]) {
        return;
    }

    visited[startVertex] = true;

    for (long vertex : graph[startVertex]) {
        if (visited[vertex]) {
            continue;
        }

        dfs(graph, vertex, visited);
    }
}
