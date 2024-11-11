const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const lines = [];

rl
    .on("line", line => lines.push(line))
    .on("close", () => {
        let [n, weights] = lines;

        n = +n;
        weights = weights?.split(' ').map(weight => +weight).slice(0, n) ?? [];

        solve(n, weights);
    });

function solve(n, weights) {
    let additionalCount = 0;

    for (const weigth of weights)
    {
        if (weigth < 30)
        {
            additionalCount++;
        }
    }

    let millilitersMilk = additionalCount * 200;
    let milkPackagesCount = Math.trunc(millilitersMilk / 900);

    if (millilitersMilk % 900 > 0)
    {
        milkPackagesCount++;
    }

    console.log(milkPackagesCount, additionalCount);
}