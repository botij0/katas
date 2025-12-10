function manufactureGifts(
  giftsToProduce: Array<{ toy: string; quantity: number }>
): string[] {
  const r = [];
  for (const prod of giftsToProduce) {
    if (prod.quantity <= 0) continue;
    for (let i = 0; i < prod.quantity; i++) {
      r.push(prod.toy);
    }
  }

  return r;
}

const production1 = [
  { toy: "car", quantity: 3 },
  { toy: "doll", quantity: 1 },
  { toy: "ball", quantity: 2 },
];

const result1 = manufactureGifts(production1);
console.log(result1);
