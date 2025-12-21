type Gift = string | number | boolean;
type Workshop = Record<string, any>;
type Path = string[];

function findGiftPath(workshop: Workshop, gift: Gift): Path {
  const path: Path = [];

  const dfs = (node: Workshop, gift: Gift, p: Path): boolean => {
    for (const [key, val] of Object.entries(node)) {
      p.push(key);
      if (val === gift) {
        return true;
      }

      if (typeof val === "object") {
        if (dfs(val, gift, p)) {
          return true;
        }
      }

      p.pop();
    }

    return false;
  };

  dfs(workshop, gift, path);

  return path;
}

const workshop = {
  storage: {
    shelf: {
      box1: "train",
      box2: "switch",
    },
    box: "car",
  },
  gift: "doll",
};

// console.log(findGiftPath(workshop, "doll"));
console.log(
  findGiftPath(
    {
      ok: true,
      nested: {
        nope: false,
        extra: {
          is: 0,
        },
      },
    },
    false
  )
);
