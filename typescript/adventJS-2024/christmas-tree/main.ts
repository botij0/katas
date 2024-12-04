function createXmasTree(height: number, ornament: string): string {
    if (height === 0 || height > 100) {
        return "";
    }
    let last_floor = 1;
    const spaces = height - 1;
    let tree = "_".repeat(spaces) + ornament + "_".repeat(spaces) + "\n";
    for (let i = 1; i < height; i++) {
        spaces - i;
        tree +=
            "_".repeat(spaces - i) +
            ornament.repeat(last_floor + 2) +
            "_".repeat(spaces - i);
        tree += "\n";
        last_floor += 2;
    }
    tree += "_".repeat(height - 1) + "#" + "_".repeat(height - 1) + "\n";
    tree += "_".repeat(height - 1) + "#" + "_".repeat(height - 1);
    return tree;
}

const tree = createXmasTree(5, "*");
console.log(tree);
