import { readFileContent } from "../utils";

interface Point {
  x: number;
  y: number;
}

const main = async () => {
  const fileContent = await readFileContent("src/09/input.txt");
  const points = getPointsList(fileContent);

  let maxArea = 0;
  for (let i = 0; i < points.length; i++) {
    for (let j = i; j < points.length - 1; j++) {
      const base = Math.abs(points[i].x - points[j].x) + 1;
      const heigth = Math.abs(points[i].y - points[j].y) + 1;

      const currentArea = base * heigth;

      if (currentArea > maxArea) maxArea = currentArea;
    }
  }

  console.log(maxArea);
};

const getPointsList = (fileContent: string): Point[] => {
  return fileContent.split("\n").map((line) => {
    const values = line.split(",").map(Number);
    return {
      x: values[0],
      y: values[1],
    };
  });
};

main();
