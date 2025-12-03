import { readFileContent } from "../utils";

const main = async () => {
  const fileContent = await readFileContent("src/03/input.txt");
  const batteries = getBatteriesList(fileContent);

  let r = 0;

  batteries.map((battery) => {
    let aux = "";
    let currentIndex = -1;
    while (aux.length < 12) {
      let value = 0;
      for (let i = currentIndex + 1; i < battery.length - (12 - aux.length - 1); i++) {
        if (battery[i] > value) {
          value = battery[i];
          currentIndex = i;
        }
      }
      aux += String(value);
    }
    r += Number(aux);
  });

  console.log(r);
};

const getBatteriesList = (fileContent: string) => {
  return fileContent.split("\n").map((battery) => {
    return battery.split("").map(Number);
  });
};

main();
