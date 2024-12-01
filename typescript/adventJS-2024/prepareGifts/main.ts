function prepareGifts(gifts: number[]): number[] {
    return gifts
        .sort((a, b) => a - b)
        .filter((value, index, self) => {
            return index === 0 || value !== self[index - 1];
        });
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

const gifts4: number[] = [-1, 80, 44, -23, 7];
const preparedGifts4: number[] = prepareGifts(gifts4);
console.log(gifts4); // []
