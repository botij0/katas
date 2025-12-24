function canEscape(maze: string[][]): boolean {
  // Code here
  const visited = new Set();
  const iStart = maze.findIndex((r) => r.includes("S"));
  const jStart = maze[iStart].indexOf("S");
  const stack = [[iStart, jStart]];

  while (stack.length > 0) {
    const node = stack.pop()!;
    const [i, j] = node;

    if (i < 0 || i >= maze.length || j < 0 || j >= maze[0].length) continue;

    if (maze[i][j] === "E") return true;

    if (maze[i][j] === "#") continue;

    if (!visited.has(node.toString())) {
      visited.add(node.toString());
      stack.push([i - 1, j]);
      stack.push([i + 1, j]);
      stack.push([i, j - 1]);
      stack.push([i, j + 1]);
    }
  }

  return false;
}

console.log(
  canEscape([
    ["S", ".", "#", "."],
    ["#", ".", "#", "."],
    [".", ".", ".", "."],
    ["#", "#", "#", "E"],
  ])
);
// → true

console.log(
  canEscape([
    ["S", "#", "#"],
    [".", "#", "."],
    [".", "#", "E"],
  ])
);
// → false

console.log(canEscape([["S", "E"]])); // true

console.log(
  canEscape([
    ["S", ".", ".", ".", "."],
    ["#", "#", "#", "#", "."],
    [".", ".", ".", ".", "."],
    [".", "#", "#", "#", "#"],
    [".", ".", ".", ".", "E"],
  ])
);
