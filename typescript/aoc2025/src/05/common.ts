interface range {
  a: number;
  b: number;
}

export const getValidRanges = (fileContent: string): range[] => {
  const ranges: range[] = [];
  fileContent
    .split("\n\n")[0]
    .split("\n")
    .map((range) => {
      const [a, b] = range.split("-").map(Number);
      ranges.push({ a, b });
    });

  ranges.sort((x, y) => x.a - y.a);
  return ranges;
};

export const getIds = (fileContent: string): number[] => {
  return fileContent
    .split("\n\n")[1]
    .split("\n")
    .map(Number)
    .sort((a, b) => a - b);
};
