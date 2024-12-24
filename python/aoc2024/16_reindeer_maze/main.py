import heapq

# TODO: REFACTOR + UNDERSTAND


def main():
    maze = read_file("puzzle_input.txt")
    for p in visit_map(maze):
        print(p)


def visit_map(maze: list[str]) -> tuple[int, int]:
    final = find_target(maze, "E")
    start = find_target(maze, "S")

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    initial_state = (0, (0, start[0], start[1]), None)
    queue = [initial_state]

    visited_pos: dict[tuple[int, int, int], int] = {}
    prev_pos: dict[tuple[int, int, int], list[tuple[int, int, int]]] = {
        initial_state[1]: []
    }
    winning_score: int | None = None
    while queue:
        score, current_node, prev_node = heapq.heappop(queue)

        if winning_score and score > winning_score:
            break

        (direction, i, j) = current_node

        if current_node in visited_pos:
            if score == visited_pos[current_node]:
                prev_pos[current_node].append(prev_node)
            continue

        visited_pos[current_node] = score

        if prev_node is not None:
            prev_pos[current_node] = [prev_node]

        if (i, j) == final:
            winning_score = score
            break

        next_i, next_j = directions[direction]

        if maze[i + next_i][j + next_j] != "#":
            heapq.heappush(
                queue, (score + 1, (direction, i + next_i, j + next_j), current_node)
            )

        for n in [-1, 1]:
            next_dir = (direction + n) % len(directions)
            heapq.heappush(queue, (score + 1000, (next_dir, i, j), current_node))

    points: set[tuple[int, int]] = set()
    nodes = [k for k in prev_pos if (k[1], k[2]) == final]
    while nodes:
        node = nodes.pop()
        points.add((node[1], node[2]))
        for n in prev_pos[node]:
            nodes.append(n)

    return winning_score, len(points)


def find_target(maze: list, target: str):
    for i, row in enumerate(maze):
        for j, char in enumerate(row):
            if char == target:
                return i, j
    return None


def read_file(filename: str) -> list[str]:
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def display_maze(maze: list[str]):
    for line in maze:
        print(line)


if __name__ == "__main__":
    main()
