function createFrame(names) {
    // Code here
    var longest = biggerString(names);
    var aux = "*";
    var s = aux.repeat(longest.length + 5);
    for (var _i = 0, names_1 = names; _i < names_1.length; _i++) {
        var name_1 = names_1[_i];
        s += "\n* " + name_1 + " *";
    }
    s += "\n";
    s += aux.repeat(longest.length + 5);
    return s;
}
function biggerString(array) {
    return array.reduce(function (biggerString, currentString) {
        return currentString.length > biggerString.length
            ? currentString
            : biggerString;
    });
}
console.log(createFrame(["midu", "madeval", "educalvolpz"]));
console.log(createFrame(["midu"]));
console.log(createFrame(["a", "bb", "ccc"]));
