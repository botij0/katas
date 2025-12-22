type Gifts = number[];
type MaxWeight = number;
type Result = number | null;

function packGifts(gifts: Gifts, maxWeight: MaxWeight): Result {
  // Code here

  let currentSled = 0;
  let totalSleds = 0;
  for (const gift of gifts) {
    if (gift > maxWeight) return null;

    if (currentSled + gift > maxWeight) {
      totalSleds += 1;
      currentSled = 0;
    }

    currentSled += gift;
  }

  return currentSled === 0 ? totalSleds : totalSleds + 1;
}

console.log(packGifts([2, 3, 4, 1], 5));
console.log(packGifts([3, 3, 2, 1], 3));
console.log(packGifts([5, 6, 1], 5));
console.log(packGifts([], 5));
