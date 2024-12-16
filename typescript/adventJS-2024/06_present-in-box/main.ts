function inBox(box: string[]): boolean {
    const mySet = new Set(box[0]);
    const mySet2 = new Set(box[box.length - 1]);
    if (mySet.size !== 1 || mySet2.size !== 1) {
        return false;
    }
    for (let i = 1; i < box.length - 1; i++) {
        if (box[i][0] !== "#" || box[i][box[i].length - 1] !== "#") {
            return false;
        }
        if (box[i].includes("*")) {
            return true;
        }
    }
    return false;
}

console.log(inBox(["###", "#*#", "###"]));
console.log(inBox(["####", "#* #", "#  #", "####"]));
console.log(inBox(["#####", "#   #", "#  #*", "#####"]));
console.log(inBox(["#####", "#   #", "#   #", "#   #", "#####"]));
