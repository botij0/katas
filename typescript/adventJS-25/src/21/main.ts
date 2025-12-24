function clearGifts(warehouse: string[][], drops: number[]): string[][] {
  // Code here
  const rowSize = warehouse[0].length;
  for (const col of drops) {
    for (let i = warehouse.length - 1; i >= 0; i--) {
      if (warehouse[i][col] === ".") {
        warehouse[i][col] = "#";
        if (!warehouse[i].includes(".")) {
          warehouse.pop();
          warehouse.unshift(new Array(rowSize).fill("."));
        }
        break;
      }
    }
  }
  return warehouse;
}

console.log(
  clearGifts(
    [
      [".", ".", "."],
      [".", ".", "."],
      ["#", ".", "#"],
    ],
    [1]
  )
);
/*
1. El regalo cae en la columna 1
2. La fila 2 se convierte en [# # #].
3. La fila 2 está completa, el robot la limpia.
6. Se añade una nueva fila vacía en la posición 0.

Resultado:
[
  ['.', '.', '.'],
  ['.', '.', '.'],
  ['.', '.', '.']
]
*/

console.log(
  clearGifts(
    [
      [".", ".", "#"],
      ["#", ".", "#"],
      ["#", ".", "#"],
    ],
    [0, 1, 2]
  )
);
/*
1. El regalo cae en la columna 0
2. El regalo cae en la columna 1
3. La fila 2 se convierte en [# # #]
4. La fila 2 está completa, el robot la limpia

Por ahora queda así:
[
  ['.', '.', '.']
  ['#', '.', '#'],
  ['#', '.', '#'],
]

5. El regalo cae en la columna 2

Resultado:
[
  ['.', '.', '#'],
  ['#', '.', '#'],
  ['#', '.', '#']
]
*/
console.log(clearGifts([["."]], [0, 0, 0]));
