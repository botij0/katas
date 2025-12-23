function revealSantaRoute(routes: string[][]): string[] {
  // Code here
  const finalRoute: string[] = routes.shift() ?? [];
  let currentLocation = finalRoute[finalRoute.length - 1];
  let nextLocation = currentLocation;

  while (routes.length >= 0) {
    for (const route of routes) {
      if (nextLocation === route[0]) {
        nextLocation = route[1];
        routes = routes.filter((r) => r !== route);
        finalRoute.push(nextLocation);
        break;
      }
    }
    if (nextLocation === currentLocation) break;
    currentLocation = nextLocation;
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
