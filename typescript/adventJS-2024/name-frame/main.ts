function createFrame(names: string[]): string {
    const longest = biggerString(names);
    let s = "*".repeat(longest.length + 4);
    for (let name of names) {
        s += "\n* " + name + " ".repeat(longest.length - name.length) + " *";
    }
    s += "\n";
    s += "*".repeat(longest.length + 4);
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
