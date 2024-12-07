function fixPackages(packages: string): string {
    const stack: string[] = [];

    for (const char of packages) {
        if (char === ")") {
            let inner = "";
            while (stack.length > 0 && stack[stack.length - 1] !== "(") {
                inner += stack.pop()!;
            }
            stack.pop();
            stack.push(...inner);
        } else {
            stack.push(char);
        }
    }
    return stack.join("");
}

console.log(fixPackages("a(cb)de"));
console.log(fixPackages("a(bc(def)g)h"));
console.log(fixPackages("abc(def(gh)i)jk"));
console.log(fixPackages("a(b(c))e"));
