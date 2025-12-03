import { readFileContent } from "../utils";

const main = async () => {
  const fileContent = await readFileContent("src/02/input.txt");
  const idsRangeList = getIdsRangeList(fileContent);

  const ids: Set<number> = new Set();
  idsRangeList.map((range) => {
    for (let i = range.start; i < range.end + 1; i++) {
      const sNumber = String(i);
      const nLength = sNumber.length;

      const dividers = getDividers(nLength);

      dividers.map((div) => {
        if (div === 1) return;

        if (div === nLength) {
          if (sNumber === sNumber[0].repeat(div)) ids.add(i);
          return;
        }

        const partition = sNumber.slice(0, div);
        if (partition.repeat(nLength / div) === sNumber) ids.add(i);
      });
    }
  });

  let r = 0;
  ids.forEach((id) => {
    r += id;
  });
  console.log(r);
};

interface Range {
  start: number;
  end: number;
}

const getDividers = (n: number): number[] => {
  const dividers: number[] = [];

  for (let i = 0; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      dividers.push(i);

      // Avoid duplicates in perfect squares.
      const other = n / i;
      if (other !== i) dividers.push(other);
    }
  }

  return dividers;
};

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
