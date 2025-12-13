type Glove = { hand: "L" | "R"; color: string };

function matchGloves(gloves: Glove[]): string[] {
  const count = Object.fromEntries(
    Array.from(new Set(gloves.map((glove) => glove.color))).map((color) => [
      color,
      { L: 0, R: 0 },
    ])
  );

  const result = [];

  for (const glove of gloves) {
    count[glove.color][glove.hand] += 1;

    if (count[glove.color].L >= 1 && count[glove.color].R) {
      result.push(glove.color);
      count[glove.color].L -= 1;
      count[glove.color].R -= 1;
    }
  }

  return result;
}

const gloves: Glove[] = [
  { hand: "L", color: "red" },
  { hand: "R", color: "red" },
  { hand: "R", color: "green" },
  { hand: "L", color: "blue" },
  { hand: "L", color: "green" },
];

console.log(matchGloves(gloves));
