import { readFileContent } from "../utils";

const main = async () => {
  const fileContent = await readFileContent("src/01/input.txt");
  const instructionsList = getInstructionsList(fileContent);

  let dialValue = 50;
  let password = 0;
  let previusDial = 50;

  instructionsList.map((instruction) => {
    const r = instruction.count % 100;
    const p = Math.floor(instruction.count / 100);
    previusDial = dialValue;

    if (instruction.direction === "L") {
      dialValue -= r;
      password += 1 * p;
      if (dialValue < 0) {
        dialValue += 100;
        if (previusDial !== 0) password += 1;
      }
    } else {
      dialValue += r;
      password += 1 * p;
      if (dialValue >= 100) {
        dialValue -= 100;
        if (dialValue !== 0) password += 1;
      }
    }

    if (dialValue === 0 && r !== 0) password += 1;
  });

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
