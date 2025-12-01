import { readFileContent } from "../utils";

const main = async () => {
  const fileContent = await readFileContent("src/01/exmaple.txt");
  console.log(fileContent);
};

main();
