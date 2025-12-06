import { readFileContent } from "../utils";

const main = async () => {
  const fileContent = await readFileContent("src/06/input.txt");
  const problems = getProblemsList(fileContent);
  let finalResult = 0;

  let r = 0;
  let operation = "";

  const maxLengthRow = problems.reduce((max, row) => Math.max(max, row.length), 0);

  for (let j = 0; j < maxLengthRow; j++) {
    const newOperation = problems[problems.length - 1][j];

    if (newOperation === "+" || newOperation === "*") {
      operation = newOperation;
      r = operation === "+" ? 0 : 1;
    }

    let currentNumber = "";
    for (let i = 0; i < problems.length - 1; i++) {
      if (problems[i][j] !== undefined) {
        currentNumber += problems[i][j];
      }
    }

    if (Number(currentNumber) !== 0) {
      if (operation === "+") {
        r += Number(currentNumber);
      } else {
        r *= Number(currentNumber);
      }
    } else {
      finalResult += r;
    }
  }
  finalResult += r;
  console.log(finalResult);
};

const getProblemsList = (fileContent: string): string[][] => {
  return fileContent.split("\n").map((row) => row.split(""));
};

main();
