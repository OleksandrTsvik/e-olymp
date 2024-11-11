s, n, b = map(int, input().split())

sponsorSum = b
lastTournamentSum = s
secondLastTournamentSum = s

for i in range(3, n):
    tempLastTournamentSum = lastTournamentSum

    lastTournamentSum = secondLastTournamentSum + lastTournamentSum + 1
    secondLastTournamentSum = tempLastTournamentSum

if n <= 2:
    sponsorSum -= n * s
else:
    sponsorSum -= secondLastTournamentSum + lastTournamentSum + 1

print(abs(sponsorSum))
