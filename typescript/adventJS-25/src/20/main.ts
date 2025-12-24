function dropGifts(warehouse: string[][], drops: number[]): string[][] {
  // Code here
  for (const col of drops) {
    for (let i = warehouse.length - 1; i >= 0; i--) {
      if (warehouse[i][col] === ".") {
        warehouse[i][col] = "#";
        break;
      }
    }
  }
  return warehouse;
}

console.log(
  dropGifts(
    [
      [".", ".", "."],
      [".", "#", "."],
      ["#", "#", "."],
    ],
    [0]
  )
);
/*
[
  ['.', '.', '.'],
  ['#', '#', '.'],
  ['#', '#', '.']
]
*/

console.log(
  dropGifts(
    [
      [".", ".", "."],
      ["#", "#", "."],
      ["#", "#", "#"],
    ],
    [0, 2]
  )
);
/*
[
  ['#', '.', '.'],
  ['#', '#', '#'],
  ['#', '#', '#']
]
*/

console.log(
  dropGifts(
    [
      ["#", "#"],
      ["#", "#"],
    ],
    [0, 0]
  )
);
/*
[
  ['#', '#']
  ['#', '#']
]
*/
