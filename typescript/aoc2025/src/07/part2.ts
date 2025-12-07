import { readFileContent } from "../utils";

const main = async () => {
  const fileContent = await readFileContent("src/07/input.txt");
  const rows = fileContent.split("\n");

  const currentTimelines = Array(rows[0].length).fill(0);
  let beans: Set<number> = new Set();
  const start = rows[0].indexOf("S");
  beans.add(start);
  currentTimelines[start] = 1;

  for (let i = 1; i < rows.length; i++) {
    if (rows[i].includes("^") === false) continue;

    const newBeans: Set<number> = new Set();

    beans.forEach((bean) => {
      if (rows[i][bean] === "^") {
        const left = bean - 1;
        const right = bean + 1;

        newBeans.add(left);
        newBeans.add(right);

        const currentBean = currentTimelines[bean];
        currentTimelines[left] += currentBean;
        currentTimelines[right] += currentBean;
        currentTimelines[bean] = 0;
      } else {
        newBeans.add(bean);
      }
    });
    beans = newBeans;
  }

  console.log(currentTimelines);

  const timeLines = currentTimelines.reduce((prev, current) => prev + current);
  console.log(timeLines);
};

main();
