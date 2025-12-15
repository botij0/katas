function findUnsafeGifts(warehouse: string[]): number {
    let validGifts = 0;

    for (let i = 0; i < warehouse.length; i++) {
        for (let j = 0; j < warehouse[i].length; j++) {
            if (warehouse[i][j] === "." || warehouse[i][j] === "#") continue;

            if (isValidGift(i, j, warehouse)) {
                validGifts += 1;
            }
        }
    }
    return validGifts;
}

const DIRECTIONS = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
] as const;

const isValidGift = (
    row: number,
    col: number,
    warehouse: string[]
): boolean => {
    return DIRECTIONS.every(([dRow, dCol]) => {
        const newRow = row + dRow;
        const newCol = col + dCol;
        const isOutOfBounds =
            newRow < 0 ||
            newRow >= warehouse.length ||
            newCol < 0 ||
            newCol >= warehouse[row].length;

        return isOutOfBounds || warehouse[newRow][newCol] !== "#";
    });
};

console.log(findUnsafeGifts([".*.", "*#*", ".*."]));
console.log(findUnsafeGifts(["...", ".*.", "..."]));
console.log(findUnsafeGifts(["*.*", "...", "*#*"]));
console.log(findUnsafeGifts(["***"]));
