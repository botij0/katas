import { readFileContent } from "../utils";
import { checkAdyacents, getRollsOfPaperGrid } from "./common";

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

main();
