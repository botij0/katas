class Master:
    def __init__(self, secret: str, allowedGuesses: int):
        self.secret = secret
        self.allowedGuesses = allowedGuesses

    def guess(self, word):
        """
        :type word: str
        :rtype int
        """
        r = 0
        for i in range(len(word)):
            if self.secret[i] == word[i]:
                r += 1
        return r


class Solution(object):
    def findSecretWord(self, words: list, master: Master):
        """
        :type words: List[Str]
        :type master: Master
        :rtype: None
        """
        tries = 0
        coincidence_word = ""
        max_coincidence = 0
        bad_words = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
        for word in words:
            if tries >= master.allowedGuesses:
                print("you failed")
                return

            if self.should_try_new_word(
                word, coincidence_word, max_coincidence, bad_words
            ):
                x = master.guess(word)
                tries += 1
                print(word, coincidence_word, tries, max_coincidence, x)

                if x == 0:
                    if len(coincidence_word) > 0:
                        coincidence_word = self.modify_coincidenc_word(
                            coincidence_word, word
                        )
                    else:
                        for i in range(6):
                            bad_words[i].append(word[i])

                if x == 6:
                    print("You guessed the secret word correctly.")
                    return

                if x > max_coincidence:
                    max_coincidence = x
                    coincidence_word = word

    def should_try_new_word(
        self, word: str, coincidence_word: str, max_coincidences: int, bad_words: dict
    ):
        if max_coincidences == 0:
            print(bad_words)
            aux = 0
            for i, c in enumerate(word):
                if c in bad_words[i]:
                    aux += 1
            print(aux)
            return True if aux != 6 else False

        coincidences = 0
        for i in range(len(word)):
            if (
                word[i] == coincidence_word[i]
                and word[i].capitalize() != coincidence_word[i]
            ):
                coincidences += 1
        return True if coincidences == max_coincidences else False

    def modify_coincidenc_word(self, coincidence_word: str, word: str):
        new_word = list(coincidence_word)

        for i in range(len(word)):
            if word[i] == coincidence_word[i]:
                new_word[i] = coincidence_word[i].capitalize()
        return "".join(new_word)


if __name__ == "__main__":
    master = Master("ccoyyo", 20)
    words = [
        "wichbx",
        "oahwep",
        "tpulot",
        "eqznzs",
        "vvmplb",
        "eywinm",
        "dqefpt",
        "kmjmxr",
        "ihkovg",
        "trbzyb",
        "xqulhc",
        "bcsbfw",
        "rwzslk",
        "abpjhw",
        "mpubps",
        "viyzbc",
        "kodlta",
        "ckfzjh",
        "phuepp",
        "rokoro",
        "nxcwmo",
        "awvqlr",
        "uooeon",
        "hhfuzz",
        "sajxgr",
        "oxgaix",
        "fnugyu",
        "lkxwru",
        "mhtrvb",
        "xxonmg",
        "tqxlbr",
        "euxtzg",
        "tjwvad",
        "uslult",
        "rtjosi",
        "hsygda",
        "vyuica",
        "mbnagm",
        "uinqur",
        "pikenp",
        "szgupv",
        "qpxmsw",
        "vunxdn",
        "jahhfn",
        "kmbeok",
        "biywow",
        "yvgwho",
        "hwzodo",
        "loffxk",
        "xavzqd",
        "vwzpfe",
        "uairjw",
        "itufkt",
        "kaklud",
        "jjinfa",
        "kqbttl",
        "zocgux",
        "ucwjig",
        "meesxb",
        "uysfyc",
        "kdfvtw",
        "vizxrv",
        "rpbdjh",
        "wynohw",
        "lhqxvx",
        "kaadty",
        "dxxwut",
        "vjtskm",
        "yrdswc",
        "byzjxm",
        "jeomdc",
        "saevda",
        "himevi",
        "ydltnu",
        "wrrpoc",
        "khuopg",
        "ooxarg",
        "vcvfry",
        "thaawc",
        "bssybb",
        "ccoyyo",
        "ajcwbj",
        "arwfnl",
        "nafmtm",
        "xoaumd",
        "vbejda",
        "kaefne",
        "swcrkh",
        "reeyhj",
        "vmcwaf",
        "chxitv",
        "qkwjna",
        "vklpkp",
        "xfnayl",
        "ktgmfn",
        "xrmzzm",
        "fgtuki",
        "zcffuv",
        "srxuus",
        "pydgmq",
    ]
    Solution().findSecretWord(words, master)
