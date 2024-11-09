#include <iostream>

using namespace std;

int main() {
    std::ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int s, n;
    long long b; // TODO: use BigInt instead of long long

    cin >> s >> n >> b;

    long long sponsorSum = b;
    long long lastTournamentSum = s;
    long long secondLastTournamentSum = s;

    for (int i = 3; i < n; i++) {
        long long tempLastTournamentSum = lastTournamentSum;

        lastTournamentSum = secondLastTournamentSum + lastTournamentSum + 1;
        secondLastTournamentSum = tempLastTournamentSum;
    }

    if (n <= 2) {
        sponsorSum -= n * s;
    } else {
        sponsorSum -= secondLastTournamentSum + lastTournamentSum + 1;
    }

    cout << abs(sponsorSum);
}
