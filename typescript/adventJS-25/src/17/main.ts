function hasFourLights(board: string[][]): boolean {
  // Code here
  const checkRow = (board: string[][], i: number, j: number) => {
    let count = 0;
    const light = board[i][j];

    let ii = i - 1;
    while (ii > 0 && count < 3) {
      if (board[ii][j] === light) count += 1;
      else break;
      ii -= 1;
    }
    ii = i + 1;

    while (ii < board.length && count < 3) {
      if (board[ii][j] === light) count += 1;
      else break;
      ii += 1;
    }

    return count >= 3 ? true : false;
  };

  const checkCol = (board: string[][], i: number, j: number) => {
    let count = 0;
    const light = board[i][j];

    let jj = j - 1;
    while (jj > 0 && count < 3) {
      if (board[i][jj] === light) count += 1;
      else break;
      jj -= 1;
    }
    jj = j + 1;

    while (jj < board[i].length && count < 3) {
      if (board[i][jj] === light) count += 1;
      else break;
      jj += 1;
    }

    return count >= 3 ? true : false;
  };

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      if (board[i][j] === ".") continue;

      if (checkRow(board, i, j)) return true;
      if (checkCol(board, i, j)) return true;
    }
  }

  return false;
}

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
