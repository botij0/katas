function inBox(box: string[]): boolean {
    const isEdgeValid = (line: string) =>
        line.split("").every((char) => char === "#");
    if (!isEdgeValid(box[0]) || !isEdgeValid(box[box.length - 1])) {
        return false;
    }

    for (let i = 1; i < box.length - 1; i++) {
        const line = box[i];
        if (line[0] !== "#" || line[line.length - 1] !== "#") {
            return false;
        }
        if (line.includes("*")) {
            return true;
        }
    }

    return false;
}

console.log(inBox(["###", "#*#", "###"]));
console.log(inBox(["####", "#* #", "#  #", "####"]));
console.log(inBox(["#####", "#   #", "#  #*", "#####"]));
console.log(inBox(["#####", "#   #", "#   #", "#   #", "#####"]));
