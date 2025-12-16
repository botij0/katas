type Board = string;
type Moves = string;
type Result = "fail" | "crash" | "success";

function moveReno(board: Board, moves: Moves): Result {
  // Code here

  type Directions = "D" | "L" | "R" | "U";

  const directions = {
    D: [1, 0],
    L: [0, -1],
    R: [0, 1],
    U: [-1, 0],
  };

  const board2d = board
    .trim()
    .split("\n")
    .map((row) => row.split(""));

  const i = board2d.findIndex((row) => row.includes("@"));
  const j = board2d[i].indexOf("@");
  let robotPosition = [i, j];

  for (let i = 0; i < moves.length; i++) {
    const currentMove = directions[moves[i] as Directions];
    robotPosition = [
      robotPosition[0] + currentMove[0],
      robotPosition[1] + currentMove[1],
    ];

    if (
      robotPosition[0] < 0 ||
      robotPosition[0] >= board2d.length ||
      robotPosition[1] < 0 ||
      robotPosition[1] >= board2d[0].length ||
      board2d[robotPosition[0]][robotPosition[1]] === "#"
    )
      return "crash";

    if (board2d[robotPosition[0]][robotPosition[1]] === "*") return "success";
  }

  return "fail";
}

const board = `
.....
.*#.*
.@...
.....
`;

console.log(moveReno(board, "L"));
console.log(moveReno(board, "RU"));
console.log(moveReno(board, "RRRUU"));
console.log(moveReno(board, "UUU"));
