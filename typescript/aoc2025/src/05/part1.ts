import { readFileContent } from "../utils";

const main = async () => {
  const fileContent = await readFileContent("src/05/input.txt");
  const validRanges = getValidRanges(fileContent);
  const ids = getIds(fileContent);

  let r = 0;

  ids.map((id) => {
    for (const range of validRanges) {
      if (id >= range.a && id <= range.b) {
        r += 1;
        break;
      }
    }
  });

  console.log(r);
};

interface range {
  a: number;
  b: number;
}

const getValidRanges = (fileContent: string): range[] => {
  const ranges: range[] = [];
  fileContent
    .split("\n\n")[0]
    .split("\n")
    .map((range) => {
      const [a, b] = range.split("-").map(Number);
      ranges.push({ a, b });
    });

  return ranges;
};

const getIds = (fileContent: string): number[] => {
  return fileContent.split("\n\n")[1].split("\n").map(Number);
};

main();
