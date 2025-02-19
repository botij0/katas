class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                aux = stack.pop()
                if matchs[c] != aux:
                    return False

        return True if len(stack) == 0 else False


if __name__ == "__main__":
    s = "([])"
    print(Solution().isValid(s))
