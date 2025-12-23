function hasFourInARow(board: string[][]): boolean {
  // Code here
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      if (board[i][j] === ".") continue;
      if (checkVertical(board, i, j)) return true;
      if (checkHorizontal(board, i, j)) return true;
      if (checkDiagonal(board, i, j)) return true;
    }
  }

  return false;
}

const checkVertical = (board: string[][], i: number, j: number) => {
  let count = 0;
  const light = board[i][j];

  // Check Up Values
  let ii = i - 1;
  while (ii >= 0 && count < 3) {
    if (board[ii][j] === light) count += 1;
    else break;
    ii -= 1;
  }

  // Check Down Values
  ii = i + 1;
  while (ii < board.length && count < 3) {
    if (board[ii][j] === light) count += 1;
    else break;
    ii += 1;
  }

  return count >= 3 ? true : false;
};

const checkHorizontal = (board: string[][], i: number, j: number) => {
  let count = 0;
  const light = board[i][j];

  // Check Left Values
  let jj = j - 1;
  while (jj >= 0 && count < 3) {
    if (board[i][jj] === light) count += 1;
    else break;
    jj -= 1;
  }

  // Check Right Values
  jj = j + 1;
  while (jj < board[i].length && count < 3) {
    if (board[i][jj] === light) count += 1;
    else break;
    jj += 1;
  }

  return count >= 3 ? true : false;
};

const checkDiagonal = (board: string[][], i: number, j: number) => {
  let count = 0;
  const light = board[i][j];

  // Check up Left Values
  let jj = j - 1;
  let ii = i - 1;
  while (jj >= 0 && ii >= 0 && count < 3) {
    if (board[ii][jj] === light) count += 1;
    else break;
    jj -= 1;
    ii -= 1;
  }

  // Check up Right Values
  jj = j + 1;
  ii = i - 1;
  while (jj < board[i].length && ii >= 0 && count < 3) {
    if (board[ii][jj] === light) count += 1;
    else break;
    jj += 1;
    ii -= 1;
  }

  // Check down Left Values
  jj = j - 1;
  ii = i + 1;
  while (jj >= 0 && ii < board.length && count < 3) {
    if (board[i][jj] === light) count += 1;
    else break;
    jj -= 1;
    ii += 1;
  }

  // Check down Right Values
  jj = j + 1;
  ii = i + 1;
  while (jj < board[i].length && ii < board.length && count < 3) {
    if (board[i][jj] === light) count += 1;
    else break;
    jj += 1;
    ii += 1;
  }

  return count >= 3 ? true : false;
};

console.log(
  hasFourInARow([
    [".", ".", ".", ".", "."],
    ["R", "R", "R", "R", "."],
    ["G", "G", ".", ".", "."],
  ])
);
// true → hay 4 luces rojas en horizontal

console.log(
  hasFourInARow([
    [".", "G", ".", "."],
    [".", "G", ".", "."],
    [".", "G", ".", "."],
    [".", "G", ".", "."],
  ])
);
// true → hay 4 luces verdes en vertical

console.log(
  hasFourInARow([
    ["R", "G", "R"],
    ["G", "R", "G"],
    ["G", "R", "G"],
  ])
);
// false → no hay 4 luces del mismo color seguidas

console.log(
  hasFourInARow([
    [".", ".", ".", "G"],
    [".", ".", "G", "."],
    [".", "G", ".", "."],
    ["G", ".", ".", "."],
  ])
);
// true
