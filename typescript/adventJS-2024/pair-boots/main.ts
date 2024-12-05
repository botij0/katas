type Shoe = {
    type: "I" | "R";
    size: number;
};

function organizeShoes(shoes: Shoe[]): number[] {
    let pairs: number[] = [];

    for (let i = 0; i < shoes.length; i++) {
        for (let j = i + 1; j < shoes.length; j++) {
            if (
                shoes[i].size === shoes[j].size &&
                shoes[i].type !== shoes[j].type
            ) {
                pairs.push(shoes[i].size);
                i += 2;
            }
        }
    }

    return pairs;
}

const shoes: Shoe[] = [
    { type: "I", size: 38 },
    { type: "R", size: 38 },
    { type: "R", size: 42 },
    { type: "I", size: 41 },
    { type: "I", size: 42 },
];

console.log(organizeShoes(shoes));

const shoes2: Shoe[] = [
    { type: "I", size: 38 },
    { type: "R", size: 38 },
    { type: "I", size: 38 },
    { type: "I", size: 38 },
    { type: "R", size: 38 },
];

console.log(organizeShoes(shoes2));

const shoes3: Shoe[] = [
    { type: "I", size: 38 },
    { type: "R", size: 36 },
    { type: "R", size: 42 },
    { type: "I", size: 41 },
    { type: "I", size: 42 },
];

console.log(organizeShoes(shoes3));
