const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const lines = [];

rl.on('line', (line) => lines.push(line)).on('close', () => {
    let [m, n] = lineToNumbers(lines[0]);
    let matrix = lines.slice(1, m + 1).map((line) => lineToNumbers(line).slice(0, n));

    solve(m, n, matrix);
});

function lineToNumbers(line) {
    return line?.split(/\s+/).map((number) => +number) ?? [];
}

function solve(rows, columns, matrix) {
    const STEP_FORWARD = 'F';
    const STEP_RIGHT = 'R';

    const maxCornsMatrix = matrix.map((corns) => [...corns]);

    for (let i = rows - 2; i >= 0; i--) {
        maxCornsMatrix[i][0] += maxCornsMatrix[i + 1][0];
    }

    for (let j = 1; j < columns; j++) {
        maxCornsMatrix[rows - 1][j] += maxCornsMatrix[rows - 1][j - 1];
    }

    for (let i = rows - 2; i >= 0; i--) {
        for (let j = 1; j < columns; j++) {
            maxCornsMatrix[i][j] += Math.max(maxCornsMatrix[i + 1][j], maxCornsMatrix[i][j - 1]);
        }
    }

    const route = [];
    let i = 0;

    for (let j = columns - 1; j >= 0; ) {
        if (j <= 0 && i >= rows - 1) break;

        if (j === 0 || (i + 1 < rows && maxCornsMatrix[i + 1][j] >= maxCornsMatrix[i][j - 1])) {
            route.push(STEP_FORWARD);
            i++;
        } else {
            route.push(STEP_RIGHT);
            j--;
        }
    }

    console.log(route.reverse().join(''));
}
