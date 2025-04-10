class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count("D") == moves.count("U") and moves.count("R") == moves.count(
            "L"
        )


if __name__ == "__main__":
    moves = "UD"
    print(Solution().judgeCircle(moves))
