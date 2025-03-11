class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aux = False
        l_a = len(a)
        l_b = len(b)
        r = ""
        n = l_a if l_a <= l_b else l_b
        for i in range(n):
            if a[l_a - i - 1] == "0" and b[l_b - i - 1] == "0":
                if aux:
                    r = "1" + r
                    aux = False
                else:
                    r = "0" + r

            elif a[l_a - i - 1] == "1" and b[l_b - i - 1] == "1":
                if aux:
                    r = "1" + r
                else:
                    r = "0" + r
                aux = True
            else:
                if aux:
                    r = "0" + r
                else:
                    r = "1" + r

        m_bin = max(a, b, key=len)
        l_bin = len(m_bin)
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


if __name__ == "__main__":
    a = "101111"
    b = "10"
    print(Solution().addBinary(a, b))
