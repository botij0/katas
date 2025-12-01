import { promises as fs } from "fs";

export const readFileContent = async (path: string) => {
  const fileContent = await fs.readFile("./src/01/example.txt", "utf8");
  return fileContent;
};
