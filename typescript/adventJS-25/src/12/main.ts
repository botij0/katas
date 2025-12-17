function elfBattle(elf1: string, elf2: string): number {
  // Code here
  let hpElf1 = 3;
  let hpElf2 = 3;

  const elfTurn = (elfA: string, elfB: string): number => {
    if (elfA === "F") return -2;

    if (elfA === "A" && elfB !== "B") return -1;

    return 0;
  };

  for (let i = 0; i < elf1.length; i++) {
    hpElf2 += elfTurn(elf1[i], elf2[i]);
    hpElf1 += elfTurn(elf2[i], elf1[i]);

    if (hpElf1 <= 0 || hpElf2 <= 0) break;
  }

  if (hpElf1 === hpElf2) return 0;

  if (hpElf1 > hpElf2) return 1;

  return 2;
}

console.log(elfBattle("AAB", "BBA"));
console.log(elfBattle("AFAB", "BBAF"));
console.log(elfBattle("AA", "FF"));
