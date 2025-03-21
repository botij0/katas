class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        r = ""
        while columnNumber > 0:
            columnNumber -= 1
            i = columnNumber % 26
            r += chr(i + ord("A"))
            columnNumber //= 26

        return "".join(reversed(r))


if __name__ == "__main__":
    columnNumber = 28
    print(Solution().convertToTitle(columnNumber))
