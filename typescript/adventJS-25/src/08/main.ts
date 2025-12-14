function findUniqueToy(toy: string): string {
  // Code here
  let uniqueLetter = "";

  const letters = Object.fromEntries(
    Array.from(new Set(toy.toLowerCase())).map((c) => [c, 0])
  );

  for (let i = 0; i < toy.length; i++) {
    letters[toy[i].toLowerCase()] += 1;
  }

  for (let i = 0; i < toy.length; i++) {
    if (letters[toy[i].toLowerCase()] === 1) {
      uniqueLetter = toy[i];
      break;
    }
  }
  return uniqueLetter;
}
console.log(findUniqueToy("Gift")); // G
console.log(findUniqueToy("aabbc")); // i
