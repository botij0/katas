function organizeShoes(shoes) {
    var pairs = [];
    for (var i = 0; i < shoes.length; i++) {
        for (var j = i + 1; j < shoes.length; j++) {
            if (shoes[i].size === shoes[j].size &&
                shoes[i].type !== shoes[j].type) {
                if (!pairs.includes(shoes[i].size)) {
                    pairs.push(shoes[i].size);
                }
            }
        }
    }
    return pairs;
}
var shoes = [
    { type: "I", size: 38 },
    { type: "R", size: 38 },
    { type: "R", size: 42 },
    { type: "I", size: 41 },
    { type: "I", size: 42 },
];
console.log(organizeShoes(shoes));
var shoes2 = [
    { type: "I", size: 38 },
    { type: "R", size: 38 },
    { type: "I", size: 38 },
    { type: "I", size: 38 },
    { type: "R", size: 38 },
];
console.log(organizeShoes(shoes2));
var shoes3 = [
    { type: "I", size: 38 },
    { type: "R", size: 36 },
    { type: "R", size: 42 },
    { type: "I", size: 41 },
    { type: "I", size: 42 },
];
console.log(organizeShoes(shoes3));
