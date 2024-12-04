console.log("Hello world!");
function createXmasTree(height, ornament) {
    if (height === 0) {
        return "";
    }
    var last_floor = 1;
    var tree = "";
    for (var i = 1; i < height; i++) {
        var spaces = height - i;
        tree += "_".repeat(spaces);
        tree += ornament.repeat(last_floor + 2);
        last_floor += 2;
        tree += "_".repeat(spaces);
        tree += "\n";
    }
    return tree;
}
var tree = createXmasTree(5, "*");
console.log(tree);
