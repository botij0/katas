function prepareGifts(gifts) {
    var sortedGifts = gifts.sort();
    var uniqueGifts = [];
    for (var i = 0; i < sortedGifts.length; i++) {
        if (i === 0 || sortedGifts[i] !== sortedGifts[i - 1]) {
            uniqueGifts.push(sortedGifts[i]);
        }
    }
    return uniqueGifts;
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
