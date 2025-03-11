class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m_bin = max(a, b, key=len)
        l_bin = len(m_bin)

        r, aux = self.get_partial_result(a, b)

        if aux:
            dif = l_bin - len(r)
            for i in range(dif):
                if m_bin[dif - i - 1] == "1":
                    r = "0" + r
                else:
                    break
            r = "1" + r

        if len(r) < l_bin:
            return m_bin[0 : l_bin - len(r)] + r
        else:
            return r

    def get_partial_result(self, a: str, b: str):
        r = ""
        aux = False
        l_a = len(a)
        l_b = len(b)

        n = l_a if l_a <= l_b else l_b
        for i in range(n):
            if a[l_a - i - 1] == b[l_b - i - 1]:
                r = self.update_equals(r, aux)
                aux = False if a[l_a - i - 1] == 0 else True
            else:
                r = self.update_not_equals(r, aux)
        return r, aux

    def update_equals(self, r: str, aux: bool):
        if aux:
            return "1" + r
        else:
            return "0" + r

    def update_not_equals(self, r: str, aux: bool):
        if aux:
            return "0" + r
        else:
            return "1" + r


if __name__ == "__main__":
    a = "101111"
    b = "10"
    print(Solution().addBinary(a, b))
