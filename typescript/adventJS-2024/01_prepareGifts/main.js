// function prepareGifts(gifts: number[]): number[] {
//     const sortedGifts = gifts.sort((a, b) => a - b);
//     const uniqueGifts: number[] = [];
//     for (let i = 0; i < sortedGifts.length; i++) {
//         if (i === 0 || sortedGifts[i] !== sortedGifts[i - 1]) {
//             uniqueGifts.push(sortedGifts[i]);
//         }
//     }
//     return uniqueGifts;
// }
function prepareGifts(gifts) {
    return gifts
        .sort(function (a, b) { return a - b; })
        .filter(function (value, index, self) {
        return index === 0 || value !== self[index - 1];
    });
}
var gifts1 = [1, 2, 3, 4, 5];
var preparedGifts1 = prepareGifts(gifts1);
console.log(preparedGifts1); // [1, 2, 3, 4, 5]
var gifts2 = [6, 5, 5, 5, 5];
var preparedGifts2 = prepareGifts(gifts2);
console.log(preparedGifts2); // [5, 6]
var gifts3 = [];
var preparedGifts3 = prepareGifts(gifts3);
console.log(preparedGifts3); // []
var gifts4 = [-1, 80, 44, -23, 7];
var preparedGifts4 = prepareGifts(gifts4);
console.log(gifts4); // []
