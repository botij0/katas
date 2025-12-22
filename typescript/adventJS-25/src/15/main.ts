type Data = Array<Record<string, string | number>>;

function drawTable(data: Data, sortBy: string): string {
  const sortedData = sortData(data, sortBy);
  const keys = Object.keys(data[0]);
  const columnWidths = getColumnWidths(sortedData, keys);

  const separator = buildSeparator(columnWidths);
  const headerRow = buildHeaderRow(columnWidths);
  const dataRows = sortedData.map((row) => buildDataRow(row, keys, columnWidths));

  return [separator, headerRow, separator, ...dataRows, separator].join("\n");
}

function sortData(data: Data, sortBy: string): Data {
  return [...data].sort((a, b) => {
    const valA = a[sortBy];
    const valB = b[sortBy];

    if (typeof valA === "number" && typeof valB === "number") {
      return valA - valB;
    }
    return String(valA).localeCompare(String(valB));
  });
}

function getColumnWidths(data: Data, keys: string[]): number[] {
  return keys.map((key) => Math.max(...data.map((row) => String(row[key]).length)));
}

function buildSeparator(widths: number[]): string {
  return "+" + widths.map((w) => "-".repeat(w + 2)).join("+") + "+";
}

function buildHeaderRow(widths: number[]): string {
  const cells = widths.map((w, i) => {
    const header = String.fromCharCode(65 + i); // A, B, C...
    return ` ${header.padEnd(w)} `;
  });
  return "|" + cells.join("|") + "|";
}

function buildDataRow(
  row: Record<string, string | number>,
  keys: string[],
  widths: number[]
): string {
  const cells = keys.map((key, i) => ` ${String(row[key]).padEnd(widths[i])} `);
  return "|" + cells.join("|") + "|";
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
// +---------+----------+
// | A       | B        |
// +---------+----------+
// | Alice   | London   |
// | Bob     | Paris    |
// | Charlie | New York |
// +---------+----------+

console.log(
  drawTable(
    [
      { gift: "Book", quantity: 5 },
      { gift: "Music CD", quantity: 1 },
      { gift: "Doll", quantity: 10 },
    ],
    "quantity"
  )
);
// +----------+----+
// | A        | B  |
// +----------+----+
// | Music CD | 1  |
// | Book     | 5  |
// | Doll     | 10 |
// +----------+----+
