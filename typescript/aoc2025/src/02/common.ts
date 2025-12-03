interface Range {
  start: number;
  end: number;
}

export const getIdsRangeList = (fileContent: string): Range[] => {
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
