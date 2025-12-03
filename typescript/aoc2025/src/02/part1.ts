import { readFileContent } from "../utils";
import { getIdsRangeList } from "./common";

const main = async () => {
  const fileContent = await readFileContent("src/02/input.txt");
  const idsRangeList = getIdsRangeList(fileContent);

  let r = 0;
  // console.log(idsRangeList);
  idsRangeList.map((range) => {
    for (let i = range.start; i < range.end + 1; i++) {
      const sNumber = String(i);
      const nLength = sNumber.length;

      if (
        nLength % 2 === 0 &&
        sNumber.slice(0, Math.floor(nLength / 2)) ===
          sNumber.slice(Math.floor(nLength / 2), nLength)
      ) {
        r += i;
      }
    }
  });

  console.log(r);
};

main();
