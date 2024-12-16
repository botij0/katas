function organizeInventory(inventory) {
    var inventoryByCategory = {};
    for (var _i = 0, inventory_1 = inventory; _i < inventory_1.length; _i++) {
        var item = inventory_1[_i];
        if (!inventoryByCategory[item.category]) {
            inventoryByCategory[item.category] = {};
        }
        if (!inventoryByCategory[item.category][item.name]) {
            inventoryByCategory[item.category][item.name] = 0;
        }
        inventoryByCategory[item.category][item.name] += item.quantity;
    }
    return inventoryByCategory;
}
var inventary = [
    { name: "doll", quantity: 5, category: "toys" },
    { name: "car", quantity: 3, category: "toys" },
    { name: "ball", quantity: 2, category: "sports" },
    { name: "car", quantity: 2, category: "toys" },
    { name: "racket", quantity: 4, category: "sports" },
];
var inventary2 = [
    { name: "book", quantity: 10, category: "education" },
    { name: "book", quantity: 5, category: "education" },
    { name: "paint", quantity: 3, category: "art" },
];
console.log(organizeInventory(inventary));
console.log(organizeInventory(inventary2));
