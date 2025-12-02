import { readFileContent } from "../utils";

const main = async () => {
  const fileContent = await readFileContent("src/01/input.txt");
  const instructionsList = getInstructionsList(fileContent);

  let dialValue = 50;
  let password = 0;

  instructionsList.map((instruction) => {
    if (instruction.direction === "L") {
      dialValue -= instruction.count % 100;
      if (dialValue < 0) dialValue += 100;
    } else {
      dialValue += instruction.count % 100;
      if (dialValue >= 100) dialValue -= 100;
    }

    if (dialValue === 0) password += 1;
  });

  console.log(instructionsList[122]);
  console.log(password);
};

type Direction = "R" | "L";
interface Instruction {
  direction: Direction;
  count: number;
}

const getInstructionsList = (fileContent: string): Instruction[] => {
  const fileContentList = fileContent.split("\n");
  let instructionsList: Instruction[] = [];

  fileContentList.map((line) => {
    instructionsList.push({
      direction: line[0] as Direction,
      count: Number(line.slice(1, line.length)),
    });
  });

  return instructionsList;
};

main();
