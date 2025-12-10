function drawGift(size: number, symbol: string): string {
  if (size < 2) return "";

  let result = "";

  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      if (i === 0 || i === size - 1 || j === 0 || j === size - 1) {
        result += symbol;
      } else {
        result += " ";
      }
    }
    if (i !== size - 1) result += "\n";
  }

  return result;
}

const g1 = drawGift(4, "*");
console.log(g1);
