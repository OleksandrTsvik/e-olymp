const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const lines = [];

rl.on('line', (line) => lines.push(line)).on('close', () => {
    let [k] = lineToNumbers(lines[0]);
    let shifts = lines.slice(1, k + 1).map((line) => lineToNumbers(line).slice(0, 2));

    solve(shifts);
});

function lineToNumbers(line) {
    return line?.split(/\s+/).map((number) => +number) ?? [];
}

function solve(shifts) {
    const WEEKDAYS = {
        Monday: 1,
        Tuesday: 2,
        Wednesday: 3,
        Thursday: 4,
        Friday: 5,
        Saturday: 6,
        Sunday: 0,
    };

    const FRIDAY_13_COUNT_IN_NORMAL_YEAR_BY_START_DAY = {
        [WEEKDAYS.Monday]: 2,
        [WEEKDAYS.Tuesday]: 2,
        [WEEKDAYS.Wednesday]: 1,
        [WEEKDAYS.Thursday]: 3,
        [WEEKDAYS.Friday]: 1,
        [WEEKDAYS.Saturday]: 1,
        [WEEKDAYS.Sunday]: 2,
    };

    const FRIDAY_13_COUNT_IN_LEAP_YEAR_BY_START_DAY = {
        [WEEKDAYS.Monday]: 2,
        [WEEKDAYS.Tuesday]: 1,
        [WEEKDAYS.Wednesday]: 2,
        [WEEKDAYS.Thursday]: 2,
        [WEEKDAYS.Friday]: 1,
        [WEEKDAYS.Saturday]: 1,
        [WEEKDAYS.Sunday]: 3,
    };

    let daysWithoutDelivery = 0;

    for (const [startYear, endYear] of shifts) {
        for (let year = startYear; year <= endYear; year++) {
            const startDay = new Date(year, 0).getDay();

            if (isLeapYear(year)) {
                daysWithoutDelivery += FRIDAY_13_COUNT_IN_LEAP_YEAR_BY_START_DAY[startDay];
            } else {
                daysWithoutDelivery += FRIDAY_13_COUNT_IN_NORMAL_YEAR_BY_START_DAY[startDay];
            }
        }
    }

    console.log(daysWithoutDelivery);
}

function isLeapYear(year) {
    return (year % 4 === 0 && year % 100 !== 0) || year % 400 === 0;
}
