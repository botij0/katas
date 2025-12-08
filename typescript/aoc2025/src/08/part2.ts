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
    numGroups: number;

    constructor(n: number) {
        this.parent = Array.from({ length: n }, (_, i) => i);
        this.rank = Array(n).fill(0);
        this.numGroups = n; // Initially, each node is its own group
    }

    find(x: number): number {
        if (this.parent[x] !== x) {
            this.parent[x] = this.find(this.parent[x]); // Path compression
        }
        return this.parent[x];
    }

    // Returns true if this union actually merged two different groups
    union(x: number, y: number): boolean {
        const px = this.find(x);
        const py = this.find(y);
        if (px === py) return false; // Already in same circuit

        // Union by rank
        if (this.rank[px] < this.rank[py]) {
            this.parent[px] = py;
        } else if (this.rank[px] > this.rank[py]) {
            this.parent[py] = px;
        } else {
            this.parent[py] = px;
            this.rank[px]++;
        }

        this.numGroups--; // Merged two groups into one
        return true;
    }

    isFullyConnected(): boolean {
        return this.numGroups === 1;
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

    for (const pair of pairs) {
        uf.union(pair.i, pair.j);

        if (uf.isFullyConnected()) {
            const pointA = points[pair.i];
            const pointB = points[pair.j];

            console.log(
                `Final connection: ${pointA.x},${pointA.y},${pointA.z} and ${pointB.x},${pointB.y},${pointB.z}`
            );
            console.log(`X coordinates: ${pointA.x} and ${pointB.x}`);
            console.log(`Result: ${pointA.x * pointB.x}`);
            break;
        }
    }
};

main();
