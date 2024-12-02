function createFrame(names: string[]): string {
    // Code here
    const longest = biggerString(names);
    const aux = "*";
    let s = aux.repeat(longest.length + 5);
    for (let name of names) {
        s += "\n* " + name + " *";
    }
    s += "\n";
    s += aux.repeat(longest.length + 5);
    return s;
}

function biggerString(array: string[]): string {
    return array.reduce((biggerString, currentString) =>
        currentString.length > biggerString.length
            ? currentString
            : biggerString
    );
}

console.log(createFrame(["midu", "madeval", "educalvolpz"]));

console.log(createFrame(["midu"]));

console.log(createFrame(["a", "bb", "ccc"]));
