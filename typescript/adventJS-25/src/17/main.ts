function hasFourLights(board: string[][]): boolean {
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[0].length; j++) {
      if (hasConsecutiveLights(i, j, 0, 1, board)) return true; // horizontal →
      if (hasConsecutiveLights(i, j, 1, 0, board)) return true; // vertical ↓
    }
  }

  return false;
}

const hasConsecutiveLights = (
  rowIndex: number,
  colIndex: number,
  dRow: number,
  dCol: number,
  board: string[][]
): boolean => {
  const light = board[rowIndex][colIndex];
  if (light === ".") return false;

  for (let step = 1; step < 4; step++) {
    const newRowIndex = rowIndex + dRow * step;
    const newColIndex = colIndex + dCol * step;

    if (newRowIndex >= board.length || newColIndex >= board[0].length) return false;
    if (board[newRowIndex][newColIndex] !== light) return false;
  }

  return true;
};

console.log(
  hasFourLights([
    [".", ".", ".", ".", "."],
    ["R", "R", "R", "R", "."],
    ["G", "G", ".", ".", "."],
  ])
);
// true → hay 4 luces rojas en horizontal

console.log(
  hasFourLights([
    [".", "G", ".", "."],
    [".", "G", ".", "."],
    [".", "G", ".", "."],
    [".", "G", ".", "."],
  ])
);
// true → hay 4 luces verdes en vertical

console.log(
  hasFourLights([
    ["R", "G", "R"],
    ["G", "R", "G"],
    ["G", "R", "G"],
  ])
);
// false → no hay 4 luces del mismo color seguidas
