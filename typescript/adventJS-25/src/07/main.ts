function drawTree(height: number, ornament: string, frequency: number): string {
  let result = "";

  let index = 1;

  for (let i = 1; i <= height; i++) {
    let treeRow = "";
    const currentRowLength = i * 2 - 1;

    for (let j = 0; j < currentRowLength; j++) {
      if ((j + index) % frequency === 0) treeRow += ornament;
      else treeRow += "*";
    }

    index += currentRowLength;

    result += " ".repeat(height - i) + treeRow + "\n";
  }

  result += " ".repeat(height - 1) + "#";

  return result;
}

console.log(drawTree(5, "o", 2));
// console.log(drawTree(3, "@", 3));
