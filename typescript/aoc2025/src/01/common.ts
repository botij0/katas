type Direction = "R" | "L";
interface Instruction {
  direction: Direction;
  count: number;
}

export const getInstructionsList = (fileContent: string): Instruction[] => {
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
