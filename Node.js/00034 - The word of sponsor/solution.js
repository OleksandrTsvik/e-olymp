const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const lines = [];

rl.on('line', (line) => lines.push(line)).on('close', () => {
    const [n, m, k] = lineToNumbers(lines[0]);
    const winnerNumbers = lineToNumbers(lines[1]).slice(0, m);
    const deliveringTimeBetweenDepartments = lines.slice(2, k + 2).map((line) => lineToNumbers(line).slice(0, 3));
    const sponsorDepartmentNumber = lineToNumbers(lines[k + 2])[0];

    solve(n, winnerNumbers, deliveringTimeBetweenDepartments, sponsorDepartmentNumber);
});

function lineToNumbers(line) {
    return line?.split(/\s+/).map((number) => +number) ?? [];
}

function solve(competitorCount, winnerNumbers, deliveringTimeBetweenDepartments, sponsorDepartmentNumber) {
    const matrix = Array(competitorCount)
        .fill()
        .map(() => Array(competitorCount).fill(-1));

    for (const [a, b, t] of deliveringTimeBetweenDepartments) {
        const rowIndex = a - 1;
        const columnIndex = b - 1;

        matrix[rowIndex][columnIndex] = t;
        matrix[columnIndex][rowIndex] = t;
    }

    const sponsorMinPaths = findMinPaths(matrix, sponsorDepartmentNumber - 1);
    const sponsorToWinnersMinPaths = sponsorMinPaths.filter((_, index) => winnerNumbers.includes(index + 1));

    if (sponsorToWinnersMinPaths.some((path) => path === Infinity)) {
        console.log('It is not fault of sponsor...');
        return;
    }

    const maxDeliveryTime = Math.max(...sponsorToWinnersMinPaths);

    console.log('The good sponsor!');
    console.log(maxDeliveryTime);
}

function findMinPaths(matrix, startVertex) {
    const rows = matrix.length;
    const dist = Array(rows).fill(Infinity);
    const queue = [];

    dist[startVertex] = 0;
    queue.push(startVertex);

    while (queue.length > 0) {
        const currentVertex = queue.shift();

        for (let i = 0; i < rows; i++) {
            if (matrix[currentVertex][i] >= 0 && dist[i] > dist[currentVertex] + matrix[currentVertex][i]) {
                dist[i] = dist[currentVertex] + matrix[currentVertex][i];
                queue.push(i);
            }
        }
    }

    return dist;
}
