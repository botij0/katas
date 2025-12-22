type Data = Array<Record<string, string | number>>;
type SortBy = string;

function drawTable(data: Data, sortBy: SortBy): string {
  // Code here

  let table = "";

  const orderData = data.sort((a, b) => {
    if (typeof a[sortBy] === "number" && typeof b[sortBy] === "number") {
      return a[sortBy] - b[sortBy];
    } else if (typeof a[sortBy] === "string" && typeof b[sortBy] === "string") {
      return a[sortBy].localeCompare(b[sortBy]);
    }
    return 0;
  });

  const getKeysMaxLength = (data: Data) => {
    const keysMaxLength = Object.fromEntries(Object.keys(data[0]).map((c) => [c, 0]));

    data.map((obj) => {
      for (const key of Object.keys(keysMaxLength)) {
        const l = String(obj[key]).length;
        if (l > keysMaxLength[key]) keysMaxLength[key] = l;
      }
    });

    return keysMaxLength;
  };

  const keysMaxLength = getKeysMaxLength(orderData);

  // Draw headers
  for (let i = 0; i < 3; i++) {
    Object.values(keysMaxLength).map((val, index) => {
      if (i === 0 || i === 2) {
        table += "+" + "-".repeat(val + 2);
      } else {
        table += "| " + String.fromCharCode(65 + index) + " ".repeat(val);
      }
    });
    table += i === 1 ? "|\n" : "+\n";
  }

  // Draw Rows
  orderData.map((obj) => {
    for (const [key, val] of Object.entries(keysMaxLength)) {
      const s = String(obj[key]);
      table += "| " + obj[key] + " ".repeat(val - s.length) + " ";
    }
    table += "|\n";
  });

  // Draw footer;
  Object.values(keysMaxLength).map((val) => {
    table += "+" + "-".repeat(val + 2);
  });
  table += "+";
  return table;
}

console.log(
  drawTable(
    [
      { name: "Charlie", city: "New York" },
      { name: "Alice", city: "London" },
      { name: "Bob", city: "Paris" },
    ],
    "name"
  )
);
