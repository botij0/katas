function drawRace(indices: number[], length: number): string {
    let s = "";
    for (let i = 0; i < indices.length; i++) {
        s += " ".repeat(indices.length - (i + 1));
        if (indices[i] < 0) {
            s += "~".repeat(length + indices[i]);
            s += "r";
            s += "~".repeat(-1 * indices[i] - 1);
        } else if (indices[i] > 0) {
            s += "~".repeat(indices[i]);
            s += "r";
            s += "~".repeat(length - indices[i] - 1);
        } else {
            s += "~".repeat(length);
        }
        s += " /" + (i + 1);
        if (i !== indices.length - 1) {
            s += "\n";
        }
    }

    return s;
}

console.log(drawRace([0, 5, -3], 10));
console.log(drawRace([2, -1, 0, 5], 8));
console.log(drawRace([3, 7, -2], 12));
