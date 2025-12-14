function drawTree(height: number, ornament: string, frequency: number): string {
  let result = "";
  let spaces = height - 1;

  let position = 0;

  for (let i = 1; i <= height * 2; i += 2) {
    let treeRow = "";
    for (let j = position + 1; j <= i + position; j++) {
      if (j % frequency === 0) treeRow += ornament;
      else treeRow += "*";
    }

    position += treeRow.length;

    result += " ".repeat(spaces) + treeRow + "\n";

    spaces -= 1;
  }

  result += " ".repeat(height - 1) + "#";

  return result;
}

console.log(drawTree(5, "o", 2));
console.log(drawTree(3, "@", 3));
