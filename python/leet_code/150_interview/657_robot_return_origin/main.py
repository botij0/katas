class Solution:
    def judgeCircle(self, moves: str) -> bool:
        initial_pos = [0, 0]
        for c in moves:
            if c == "U":
                initial_pos[1] += 1
            elif c == "D":
                initial_pos[1] -= 1
            elif c == "R":
                initial_pos[0] += 1
            elif c == "L":
                initial_pos[0] -= 1

        return initial_pos == [0, 0]


if __name__ == "__main__":
    moves = "UD"
    print(Solution().judgeCircle(moves))
