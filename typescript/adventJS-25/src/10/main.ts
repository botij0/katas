function maxDepth(s: string): number {
  // Code here
  let maxDepth = 0;
  let currentDepth = 0;

  for (const char of s) {
    if (char === "[") {
      currentDepth++;
      if (currentDepth > maxDepth) {
        maxDepth = currentDepth;
      }
    } else if (char === "]") {
      if (currentDepth === 0) {
        return -1;
      }
      currentDepth--;
    }
  }

  return currentDepth === 0 ? maxDepth : -1;
}

// console.log(maxDepth("[]")); // -> 1
// console.log(maxDepth("][]")); // -> -1
console.log(maxDepth("[[[]][]]")); // -> -1

// console.log(maxDepth("[[]]")); // -> 2
// console.log(maxDepth("[][]")); // -> 1
// console.log(maxDepth("[[][]]")); // -> 2
// console.log(maxDepth("[[[]]]")); // -> 3
// console.log(maxDepth("[][[]][]")); // -> 2

// console.log(maxDepth("][")); // -> -1 (cierra antes de abrir)
// console.log(maxDepth("[[[")); // -> -1 (faltan cierres)
// console.log(maxDepth("[]]]")); // -> -1 (sobran cierres)
// console.log(maxDepth("[][][")); // -> -1 (queda uno sin cerrar)
