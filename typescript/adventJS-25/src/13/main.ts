type Factory = string[];
type Result = "completed" | "broken" | "loop";

function runFactory(factory: Factory): Result {
  // Code here
  const moves: { [key: string]: number[] } = {
    ">": [0, 1],
    "<": [0, -1],
    "^": [-1, 0],
    v: [1, 0],
  };

  let presentPos = [0, 0];
  const positions = new Set();
  positions.add(presentPos.toString());

  while (
    presentPos[0] < factory.length &&
    presentPos[0] >= 0 &&
    presentPos[1] < factory[0].length &&
    presentPos[1] >= 0
  ) {
    const current = factory[presentPos[0]][presentPos[1]];
    if (current === ".") {
      return "completed";
    }

    const move = moves[current];
    presentPos = [presentPos[0] + move[0], presentPos[1] + move[1]];

    if (positions.has(presentPos.toString())) return "loop";

    positions.add(presentPos.toString());
  }

  return "broken";
}

console.log(runFactory([">>."]));
console.log(runFactory([">>v", "<<<"]));
console.log(runFactory(["v.", "^."]));
