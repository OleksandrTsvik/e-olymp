const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const lines = [];

rl.on('line', (line) => lines.push(line)).on('close', () => {
    let [passengerCount, startingTicketNumber] = lines[0].split(/\s+/);

    passengerCount = parseInt(passengerCount);
    startingTicketNumber = parseInt(startingTicketNumber);

    solve(passengerCount, startingTicketNumber);
});

function solve(passengerCount, startingTicketNumber) {
    // const ticketDigitsCount = startingTicketNumber.toString().length;
    // const maxTicketNumber = Math.pow(10, ticketDigitsCount);

    passengerCount -= 2;
    let skipPassengersCount = 0;

    for (let i = 1; i <= passengerCount; i++) {
        const ticketNumber = startingTicketNumber + i;

        // if (ticketNumber >= maxTicketNumber) break;

        if (isPrimeNumber(ticketNumber)) {
            console.log(skipPassengersCount);
            return;
        }

        skipPassengersCount++;
    }

    console.log(-1);
}

function isPrimeNumber(number) {
    if (number <= 1) return false;
    if (number > 2 && number % 2 === 0) return false;

    const maxNumberToCheck = Math.sqrt(number) + 1;

    for (let i = 3; i < maxNumberToCheck; i += 2) {
        if (number % i === 0) {
            return false;
        }
    }

    return true;
}
