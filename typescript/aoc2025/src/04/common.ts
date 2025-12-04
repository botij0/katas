export const getRollsOfPaperGrid = (fileContent: string): string[][] => {
  return fileContent.split("\n").map((battery) => {
    return battery.split("");
  });
};

export const checkAdyacents = (i: number, j: number, grid: string[][]) => {
  let count = 0;

  outer: for (let ii = i - 1; ii < i + 2; ii++) {
    if (ii < 0 || ii >= grid.length) continue;

    for (let jj = j - 1; jj < j + 2; jj++) {
      if (jj < 0 || jj >= grid[0].length || (jj === j && ii === i)) continue;

      if (grid[ii][jj] === "@" || grid[ii][jj] === "X") count += 1;

      if (count >= 4) break outer;
    }
  }

  if (count < 4) {
    grid[i][j] = "X";
  }

  return count >= 4 ? 0 : 1;
};
