import { readFileContent } from "../utils";
import { getIds, getValidRanges } from "./common";

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

main();
