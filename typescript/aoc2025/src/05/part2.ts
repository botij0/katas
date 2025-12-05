import { readFileContent } from "../utils";
import { getIds, getValidRanges } from "./common";

const main = async () => {
  const fileContent = await readFileContent("src/05/input.txt");
  const validRanges = getValidRanges(fileContent);

  let r = 0;
  let lastMaxVal = 0;

  validRanges.map((range) => {
    if (range.a > lastMaxVal) {
      r += range.b - range.a + 1;
    }

    if (range.a <= lastMaxVal && range.b >= lastMaxVal) {
      r += range.b - lastMaxVal;
    }

    if (range.a < lastMaxVal && range.b < lastMaxVal) return;

    lastMaxVal = range.b;
  });
};

main();
