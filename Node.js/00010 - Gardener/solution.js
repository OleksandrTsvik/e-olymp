const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const lines = [];

rl.on('line', (line) => lines.push(line)).on('close', () => {
    let [n] = lines;

    n = +n;

    solve(n);
});

function solve(treeCount) {
    const TOTAL_AMOUNT_WATER_FOR_ONE_TREE = 0.5;

    let daysWithWatering = 0;
    let amountWaterSpilledForOneTree = 0;

    for (let i = 0; i < treeCount; i++) {
        amountWaterSpilledForOneTree += 1 / (treeCount - i);

        if (amountWaterSpilledForOneTree > TOTAL_AMOUNT_WATER_FOR_ONE_TREE) {
            break;
        }

        daysWithWatering++;
    }

    console.log(treeCount - daysWithWatering);
}
