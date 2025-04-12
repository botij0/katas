from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        r = []
        for op in operations:
            if op == "C":
                r.pop()
            elif op == "D":
                r.append(r[-1] * 2)
            elif op == "+":
                r.append(r[-1] + r[-2])
            else:
                r.append(int(op))

        return sum(r)


if __name__ == "__main__":
    ops = ["5", "2", "C", "D", "+"]
    print(Solution().calPoints(ops))
