class Solution:
    def intToRoman(self, num: int) -> str:
        r = ""
        while num > 0:
            if num >= 1000:
                r += "M"
                num -= 1000
            elif num >= 500:
                if num // 900 == 1:
                    r += "CM"
                    num -= 900
                else:
                    r += "D"
                    num -= 500
            elif num >= 100:
                if num // 400 == 1:
                    r += "CD"
                    num -= 400
                else:
                    r += "C"
                    num -= 100
            elif num >= 50:
                if num // 90 == 1:
                    r += "XC"
                    num -= 90
                else:
                    r += "L"
                    num -= 50
            elif num >= 10:
                if num // 40 == 1:
                    r += "XL"
                    num -= 40
                else:
                    r += "X"
                    num -= 10
            elif num >= 5:
                if num // 9 == 1:
                    r += "IX"
                    num -= 9
                else:
                    r += "V"
                    num -= 5
            else:
                if num // 4 == 1:
                    r += "IV"
                    num -= 4
                else:
                    r += "I"
                    num -= 1
        return r


if __name__ == "__main__":
    num = 1994
    print(Solution().intToRoman(num))
