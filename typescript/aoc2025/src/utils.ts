import { promises as fs } from "fs";

export const readFileContent = async (path: string) => {
  const fileContent = await fs.readFile(path, "utf8");
  return fileContent;
};
