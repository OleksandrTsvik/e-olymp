const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const lines = [];

rl.on('line', (line) => lines.push(line)).on('close', () => {
    let [n] = lines;

    n = +n;

    solve(+n);
});

function solve(number) {
    const numberStr = number.toString();
    const iterationCount = Math.ceil(numberStr.length / 2);
    let degreeSymmetry = 0;

    for (let i = 0; i < iterationCount; i++) {
        if (numberStr[i] === numberStr[numberStr.length - i - 1]) {
            degreeSymmetry++;
        }
    }

    console.log(degreeSymmetry);
}
