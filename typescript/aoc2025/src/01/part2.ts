import { readFileContent } from "../utils";
import { getInstructionsList } from "./common";

const main = async () => {
  const fileContent = await readFileContent("src/01/input.txt");
  const instructionsList = getInstructionsList(fileContent);

  let dialValue = 50;
  let password = 0;
  let previusDial = 50;

  instructionsList.map((instruction) => {
    const rest = instruction.count % 100;
    const cocient = Math.floor(instruction.count / 100);
    previusDial = dialValue;

    const sign = instruction.direction === "L" ? -1 : 1;
    dialValue += rest * sign;
    password += 1 * cocient;

    if (dialValue < 0 || dialValue >= 100) {
      dialValue -= 100 * sign;
      if (previusDial !== 0 && dialValue !== 0) password += 1;
    }

    if (dialValue === 0 && rest !== 0) password += 1;
  });

  console.log(password);
};

main();
