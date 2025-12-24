function revealSantaRoute(routes: string[][]): string[] {
  // Code here
  const finalRoute: string[] = routes.shift() ?? [];
  let currentLocation = finalRoute[finalRoute.length - 1];

  const routesMap = new Map(routes.map((r) => [r[0], r[1]]));
  while (routesMap.get(currentLocation) !== undefined) {
    currentLocation = routesMap.get(currentLocation)!;
    finalRoute.push(currentLocation);
  }

  return finalRoute;
}

console.log(
  revealSantaRoute([
    ["MEX", "CAN"],
    ["UK", "GER"],
    ["CAN", "UK"],
  ])
);
// → ['MEX', 'CAN', 'UK', 'GER']

console.log(
  revealSantaRoute([
    ["USA", "BRA"],
    ["JPN", "PHL"],
    ["BRA", "UAE"],
    ["UAE", "JPN"],
    ["CMX", "HKN"],
  ])
);
// → ['USA', 'BRA', 'UAE', 'JPN', 'PHL']

console.log(
  revealSantaRoute([
    ["STA", "HYD"],
    ["ESP", "CHN"],
  ])
);
// → ['STA', 'HYD']
