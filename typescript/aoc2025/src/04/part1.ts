import { readFileContent } from "../utils";

const main = async () => {
  const fileContent = await readFileContent("src/04/input.txt");
  const grid = getRollsOfPaperGrid(fileContent);

  const nRows = grid.length;
  const nCols = grid[0].length;

  let r = 0;
  for (let i = 0; i < nRows; i++) {
    for (let j = 0; j < nCols; j++) {
      if (grid[i][j] === ".") continue;
      r += checkAdyacents(i, j, grid);
    }
  }
  console.log(r);
  // console.log(grid);
};

const checkAdyacents = (i: number, j: number, grid: string[][]) => {
  let count = 0;

  for (let ii = i - 1; ii < i + 2; ii++) {
    if (ii < 0 || ii >= grid.length) continue;
    for (let jj = j - 1; jj < j + 2; jj++) {
      if (jj < 0 || jj >= grid[0].length || (jj === j && ii === i)) continue;

      if (grid[ii][jj] === "@" || grid[ii][jj] === "X") count += 1;

      if (count >= 4) break;
    }
    if (count >= 4) break;
  }
  if (count < 4) {
    grid[i][j] = "X";
  }
  return count >= 4 ? 0 : 1;
};

const getRollsOfPaperGrid = (fileContent: string) => {
  return fileContent.split("\n").map((battery) => {
    return battery.split("");
  });
};

main();
