import { readFileContent } from "../utils";

const main = async () => {
  const fileContent = await readFileContent("src/06/input.txt");
  const problems = getProblemsList(fileContent);

  let finalResult = 0;

  for (let j = 0; j < problems[0].length; j++) {
    const operation = problems[problems.length - 1][j];
    let r = operation === "+" ? 0 : 1;
    for (let i = 0; i < problems.length - 1; i++) {
      if (operation === "+") {
        r += Number(problems[i][j]);
      } else {
        r *= Number(problems[i][j]);
      }
    }
    finalResult += r;
  }

  console.log(finalResult);
};

const getProblemsList = (fileContent: string): string[][] => {
  return fileContent
    .split("\n")
    .map((row) => row.split(" ").filter((str) => str.trim() !== ""));
};

main();
