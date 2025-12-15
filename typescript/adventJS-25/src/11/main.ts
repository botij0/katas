function findUnsafeGifts(warehouse: string[]): number {
  let validGifts = 0;

  for (let i = 0; i < warehouse.length; i++) {
    for (let j = 0; j < warehouse[i].length; j++) {
      if (warehouse[i][j] === "." || warehouse[i][j] === "#") continue;

      if (
        (i === 0 || warehouse[i - 1][j] !== "#") &&
        (j === 0 || warehouse[i][j - 1] !== "#") &&
        (j === warehouse[i].length - 1 || warehouse[i][j + 1] !== "#") &&
        (i === warehouse.length - 1 || warehouse[i + 1][j] !== "#")
      ) {
        validGifts += 1;
      }
    }
  }
  return validGifts;
}

console.log(findUnsafeGifts([".*.", "*#*", ".*."]));
console.log(findUnsafeGifts(["...", ".*.", "..."]));
console.log(findUnsafeGifts(["*.*", "...", "*#*"]));
console.log(findUnsafeGifts(["***"]));
