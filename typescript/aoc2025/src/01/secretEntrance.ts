import { readFileContent } from "../utils";
import { getInstructionsList } from "./common";

const main = async () => {
  const fileContent = await readFileContent("src/01/input.txt");
  const instructionsList = getInstructionsList(fileContent);

  let dialValue = 50;
  let password = 0;

  instructionsList.map((instruction) => {
    const sign = instruction.direction === "L" ? -1 : 1;
    dialValue += (instruction.count % 100) * sign;

    if (dialValue < 0) dialValue += 100;
    if (dialValue >= 100) dialValue -= 100;

    if (dialValue === 0) password += 1;
  });

  console.log(password);
};

main();
