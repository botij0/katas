function filterGifts(gifts: string[]): string[] {
  // Code here
  return gifts.filter((gift) => gift.indexOf("#") === -1);
}

const gifts1 = ["car", "doll#arm", "ball", "#train"];
const good1 = filterGifts(gifts1);
console.log(good1);
