function decodeSantaPin(code: string): string | null {
  const blocks = code.match(/\[[^\]]+\]/g);

  if (!blocks || blocks.length < 4) return null;

  let result = "";

  for (const block of blocks) {
    const content = block.slice(1, -1); // Remove brackets

    if (content === "<") {
      result += result.at(-1) ?? "";
    } else {
      let digit = parseInt(content[0], 10);

      for (const op of content.slice(1)) {
        digit = (digit + (op === "+" ? 1 : 9)) % 10;
      }

      result += digit;
    }
  }

  return result.length >= 4 ? result : null;
}

console.log(decodeSantaPin("[1++][2-][3+][<]")); // "3144"
console.log(decodeSantaPin("[9+][0-][4][<]")); // "0944"
console.log(decodeSantaPin("[1+][2-]")); // null
