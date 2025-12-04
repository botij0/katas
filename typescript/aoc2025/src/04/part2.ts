import { readFileContent } from "../utils";
import { checkAdyacents, getRollsOfPaperGrid } from "./common";

const main = async () => {
  const fileContent = await readFileContent("src/04/input.txt");
  const grid = getRollsOfPaperGrid(fileContent);

  const nRows = grid.length;
  const nCols = grid[0].length;

  let finalResult = 0;
  let currentResult = -1;

  while (currentResult !== 0) {
    const indexModified = [];
    currentResult = 0;

    for (let i = 0; i < nRows; i++) {
      for (let j = 0; j < nCols; j++) {
        if (grid[i][j] === ".") continue;

        const val = checkAdyacents(i, j, grid);

        if (val === 1) {
          indexModified.push([i, j]);
          currentResult += val;
        }
      }
    }

    indexModified.map(([i, j]) => {
      grid[i][j] = ".";
    });

    finalResult += currentResult;
  }

  console.log(finalResult);
  // console.log(grid);
};

main();
