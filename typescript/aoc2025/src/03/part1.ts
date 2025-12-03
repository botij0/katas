import { readFileContent } from "../utils";

const main = async () => {
  const fileContent = await readFileContent("src/03/input.txt");
  const batteries = getBatteriesList(fileContent);

  let r = 0;

  batteries.map((battery) => {
    let left = 0;
    let iLeft = 0;
    let right = 0;

    for (let i = 0; i < battery.length - 1; i++) {
      if (battery[i] > left) {
        left = battery[i];
        iLeft = i;
      }
    }

    for (let i = iLeft + 1; i < battery.length; i++) {
      if (battery[i] > right) {
        right = battery[i];
      }
    }

    r += Number(`${left}${right}`);
  });

  console.log(r);
};

const getBatteriesList = (fileContent: string) => {
  return fileContent.split("\n").map((battery) => {
    return battery.split("").map(Number);
  });
};

main();
