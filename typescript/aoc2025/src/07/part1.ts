import { readFileContent } from "../utils";

const main = async () => {
  const fileContent = await readFileContent("src/07/input.txt");
  const rows = fileContent.split("\n");

  let beans: Set<number> = new Set();
  const start = rows[0].indexOf("S");
  beans.add(start);

  let splitCount = 0;

  for (let i = 1; i < rows.length; i++) {
    if (rows[i].includes("^") === false) continue;

    const newBeans: Set<number> = new Set();

    beans.forEach((bean) => {
      if (rows[i][bean] === "^") {
        splitCount += 1;

        const left = bean - 1;
        const right = bean + 1;

        if (left >= 0) newBeans.add(left);
        if (right < rows.length) newBeans.add(right);
      } else {
        newBeans.add(bean);
      }
    });
    beans = newBeans;
  }

  console.log(splitCount);
};

main();
