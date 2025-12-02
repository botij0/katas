import { readFileContent } from "../utils";

const main = async () => {
  const fileContent = await readFileContent("src/02/example.txt");
  const idsRangeList = getIdsRangeList(fileContent);

  let r = 0;
  idsRangeList.map((range) => {
    if (range.start % 2 !== 0 && range.end % 2 !== 0) return;

    for (let i = range.start; i < range.end + 1; i++) {
      const sNumber = String(i);
      const nLength = sNumber.length;

      // console.log(
      //   i,
      //   sNumber.slice(0, Math.floor(nLength / 2)),
      //   sNumber.slice(Math.floor(nLength / 2), nLength)
      // );
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

interface Range {
  start: number;
  end: number;
}

const getIdsRangeList = (fileContent: string): Range[] => {
  const idsRangeList: Range[] = [];
  fileContent.split(",").map((ranges) => {
    const [start, end] = ranges.split("-");
    idsRangeList.push({
      start: Number(start),
      end: Number(end),
    });
  });

  return idsRangeList;
};

main();
