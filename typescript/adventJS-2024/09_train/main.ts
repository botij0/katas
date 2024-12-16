type Space = "·" | "@" | "*" | "o";
type Board = String[];
type Movement = "U" | "D" | "R" | "L";
type Result = "none" | "crash" | "eat";

function moveTrain(board: Board, mov: Movement): Result {
    const [i, j] =
        board
            .map((row, x) => [x, row.indexOf("@")])
            .find(([x, o]) => o !== -1) ?? [];
    if (i === -1 || j === -1) return "none";

    const directions: Record<Movement, [number, number]> = {
        U: [-1, 0],
        D: [1, 0],
        L: [0, -1],
        R: [0, 1],
    };
    const [di, dj] = directions[mov];
    const ni = i + di;
    const nj = j + dj;
    console.log(ni, nj);
    if (ni < 0 || ni > board.length - 1 || nj < 0 || nj > board[0].length - 1)
        return "crash";
    const targetCell = board[ni][nj];

    return targetCell === "o" ? "crash" : targetCell === "*" ? "eat" : "none";
}

const board = ["·····", "*····", "@····", "o····", "o····"];

console.log(moveTrain(board, "U"));
console.log(moveTrain(board, "D"));
console.log(moveTrain(board, "L"));
console.log(moveTrain(board, "R"));
