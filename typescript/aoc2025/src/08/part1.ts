import { readFileContent } from "../utils";

interface Point {
  id: number;
  x: number;
  y: number;
  z: number;
}

interface Pair {
  i: number;
  j: number;
  distance: number;
}

// Union-Find data structure to track circuits
class UnionFind {
  parent: number[];
  rank: number[];

  constructor(n: number) {
    this.parent = Array.from({ length: n }, (_, i) => i);
    this.rank = Array(n).fill(0);
  }

  find(x: number): number {
    if (this.parent[x] !== x) {
      this.parent[x] = this.find(this.parent[x]); // Path compression
    }
    return this.parent[x];
  }

  union(x: number, y: number): void {
    const px = this.find(x);
    const py = this.find(y);
    if (px === py) return; // Already in same circuit

    // Union by rank
    if (this.rank[px] < this.rank[py]) {
      this.parent[px] = py;
    } else if (this.rank[px] > this.rank[py]) {
      this.parent[py] = px;
    } else {
      this.parent[py] = px;
      this.rank[px]++;
    }
  }

  getGroupSizes(): number[] {
    const groups = new Map<number, number>();
    for (let i = 0; i < this.parent.length; i++) {
      const root = this.find(i);
      groups.set(root, (groups.get(root) || 0) + 1);
    }
    return Array.from(groups.values());
  }
}

const getDistance3D = (a: Point, b: Point): number => {
  return Math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2);
};

const getPointsList = (fileContent: string): Point[] => {
  return fileContent.split("\n").map((line, i) => {
    const values = line.split(",").map(Number);
    return {
      id: i,
      x: values[0],
      y: values[1],
      z: values[2],
    };
  });
};

const main = async () => {
  const fileContent = await readFileContent("src/08/input.txt");
  const points = getPointsList(fileContent);

  const pairs: Pair[] = [];
  for (let i = 0; i < points.length; i++) {
    for (let j = i + 1; j < points.length; j++) {
      pairs.push({
        i: points[i].id,
        j: points[j].id,
        distance: getDistance3D(points[i], points[j]),
      });
    }
  }

  pairs.sort((a, b) => a.distance - b.distance);

  const uf = new UnionFind(points.length);
  const connectionsToMake = 1000;

  for (let c = 0; c < connectionsToMake; c++) {
    const pair = pairs[c];
    uf.union(pair.i, pair.j);
  }

  const sizes = uf.getGroupSizes().sort((a, b) => b - a);
  console.log("Circuit sizes:", sizes);
  console.log("Number of circuits:", sizes.length);

  const result = sizes[0] * sizes[1] * sizes[2];
  console.log("Result:", result);
};

main();
