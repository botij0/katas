function prepareGifts(gifts: number[]): number[] {
    const sortedGifts = gifts.sort();
    const uniqueGifts: number[] = [];
    for (let i = 0; i < sortedGifts.length; i++) {
        if (i === 0 || sortedGifts[i] !== sortedGifts[i - 1]) {
            uniqueGifts.push(sortedGifts[i]);
        }
    }
    return uniqueGifts;
}

const gifts1: number[] = [1, 2, 3, 4, 5];
const preparedGifts1: number[] = prepareGifts(gifts1);
console.log(preparedGifts1); // [1, 2, 3, 4, 5]

const gifts2: number[] = [6, 5, 5, 5, 5];
const preparedGifts2: number[] = prepareGifts(gifts2);
console.log(preparedGifts2); // [5, 6]

const gifts3: number[] = [];
const preparedGifts3: number[] = prepareGifts(gifts3);
console.log(preparedGifts3); // []
