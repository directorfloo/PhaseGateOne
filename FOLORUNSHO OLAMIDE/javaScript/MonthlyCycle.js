function nextPeriodCycle(lastMenstrualPeriodStartDate, cycleLength, periodLength) {
    let nextPeriod = lastMenstrualPeriodStartDate + cycleLength;
    return nextPeriod;
}

function ovulationCycle(lastMenstrualPeriodStartDate, cycleLength, periodLength) {
    let ovulation = lastMenstrualPeriodStartDate + (cycleLength - 14);
    return ovulation;
}

function fertileWindowCycle(ovulation) {
    let fertileStart = ovulation - 5;
    let fertileEnd = ovulation + 1;
    return [fertileStart, fertileEnd];
}

function safePeriod(ovulation, lastMenstrualPeriodStartDate, nextPeriod) {
    let safeBeforeFertileWindow = lastMenstrualPeriodStartDate;
    let safeBeforeEnd = ovulation - 6;

    let safeAfterStart = ovulation + 2;
    let safeAfterEnd = nextPeriod;

    return [safeBeforeFertileWindow, safeBeforeEnd, safeAfterStart, safeAfterEnd];
}

let lastMenstrualPeriodStartDate = 1;
let cycleLength = 28;
let periodLength = 5;

let nextPeriod = nextPeriodCycle(lastMenstrualPeriodStartDate, cycleLength, periodLength);
let ovulation = ovulationCycle(lastMenstrualPeriodStartDate, cycleLength, periodLength);
let fertile = fertileWindowCycle(ovulation);
let safe = safePeriod(ovulation, lastMenstrualPeriodStartDate, nextPeriod);

console.log("Next Period starts on day: " + nextPeriod);
console.log("Ovulation on day: " + ovulation);
console.log("Fertile Window: day " + fertile[0] + " to day " + fertile[1]);
console.log("Safe Periods:");
console.log("   Safe before fertile: day " + safe[0] + " to day " + safe[1]);
console.log("   Safe after fertile: day " + safe[2] + " to day " + safe[3]);
