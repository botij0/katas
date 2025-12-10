function decodeSantaPin(code: string): string | null {
  const regexNum = /\d{1}[+-]*|[\<]/g;
  const passwordElements = code.match(regexNum);

  if (!passwordElements || passwordElements.length < 4) return null;

  let result = "";
  for (let i = 0; i < passwordElements.length; i++) {
    const currentEl = passwordElements[i];
    if (currentEl === "<") {
      if (i !== 0) {
        result += result[i - 1];
      }
    } else {
      let n = Number(currentEl[0]);
      const signs = currentEl.slice(1);

      for (let j = 0; j < signs.length; j++) {
        if (signs[j] === "+") n += 1;
        else n -= 1;

        if (n > 9) n = 0;
        if (n < 0) n = 9;
      }
      result += n;
    }
  }

  return result;
}

const x = decodeSantaPin("[9++][0-][4][<]"); // Expected: "0944"

console.log(x);
