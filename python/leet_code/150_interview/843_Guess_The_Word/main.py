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
        words = self.sort_max_diff(words)
        print(words)
        tries = 0
        coincidence_word = ""
        max_coincidence = 0
        bad_letters = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
        for word in words:
            if tries >= master.allowedGuesses:
                print("you failed")
                return

            coincidence_word, max_coincidence, tries = self.word_try(
                word,
                master,
                bad_letters,
                max_coincidence,
                coincidence_word,
                tries,
            )

            if max_coincidence == 6:
                print(
                    "You guessed the secret word correctly. Secret word is",
                    coincidence_word,
                    tries,
                )
                return

    def word_try(
        self,
        word: str,
        master: Master,
        bad_letters: dict,
        max_coincidence: int,
        coincidence_word: str,
        tries: int,
    ):
        if self.should_try_new_word(
            word, coincidence_word, max_coincidence, bad_letters
        ):
            current_coincidences = master.guess(word)
            tries += 1
            print(word, coincidence_word, tries, max_coincidence, current_coincidences)

            if current_coincidences == 0:
                self.update_bad_letters(coincidence_word, word, bad_letters)

            if current_coincidences == 6:
                return word, current_coincidences, tries

            if current_coincidences > max_coincidence:
                max_coincidence = current_coincidences
                coincidence_word = word

        return coincidence_word, max_coincidence, tries

    def should_try_new_word(
        self,
        word: str,
        coincidence_word: str,
        max_coincidences: int,
        bad_letters: dict,
    ):
        if self.check_bad_letters(word, bad_letters):
            return False
        if not self.check_same_coincidences(coincidence_word, word, max_coincidences):
            return False
        return True

    def check_bad_letters(self, word: str, bad_letters: dict) -> bool:
        bad_letters_count = 0
        for i, c in enumerate(word):
            if c in bad_letters[i]:
                bad_letters_count += 1

        return True if bad_letters_count > 0 else False

    def check_same_coincidences(
        self, coincidence_word: str, word: str, max_coincidences: int
    ) -> bool:
        coincidences = 0
        for i in range(len(coincidence_word)):
            if word[i] == coincidence_word[i]:
                coincidences += 1

        return True if coincidences == max_coincidences else False

    def update_bad_letters(self, coincidence_word: str, word: str, bad_letters: dict):
        if len(coincidence_word) > 0:
            bad_letters_coinc = self.get_bad_letters_coincidence(coincidence_word, word)
            for letter in bad_letters_coinc:
                bad_letters[letter[0]].append(letter[1])

        else:
            for i in range(6):
                bad_letters[i].append(word[i])

    def get_bad_letters_coincidence(self, coincidence_word: str, word: str) -> list:
        bad_letters_coincidence = []

        for i in range(len(word)):
            if word[i] == coincidence_word[i]:
                bad_letters_coincidence.append((i, coincidence_word[i]))
        return bad_letters_coincidence

    def sort_max_diff(self, arr: list) -> list:
        arr.sort()
        r = []
        while arr:
            r.append(arr.pop(-1))
            if arr:
                r.append(arr.pop(0))
        return r


if __name__ == "__main__":
    master = Master("vftnkr", 12)
    words = [
        "mjpsce",
        "giwiyk",
        "slbnia",
        "pullbr",
        "ezvczd",
        "dwkrmt",
        "qgzebh",
        "wvhhlm",
        "kqbmny",
        "zpvrkz",
        "pdwxvy",
        "gilywa",
        "gmrrdc",
        "vvqvla",
        "rmjirt",
        "qmvykq",
        "mhbmuq",
        "unplzn",
        "qkcied",
        "eignxg",
        "fbfgng",
        "xpizga",
        "twubzr",
        "nnfaxr",
        "skknhe",
        "twautl",
        "nglrst",
        "mibyks",
        "qrbmpx",
        "ukgjkq",
        "mhxxfb",
        "deggal",
        "bwpvsp",
        "uirtak",
        "tqkzfk",
        "hfzawa",
        "jahjgn",
        "mteyut",
        "jzbqbv",
        "ttddtf",
        "auuwgn",
        "untihn",
        "gbhnog",
        "zowaol",
        "feitjl",
        "omtiur",
        "kwdsgx",
        "tggcqq",
        "qachdn",
        "dixtat",
        "hcsvbw",
        "chduyy",
        "gpdtft",
        "bjxzky",
        "uvvvko",
        "jzcpiv",
        "gtyjau",
        "unsmok",
        "vfcmhc",
        "hvxnut",
        "orlwku",
        "ejllrv",
        "jbrskt",
        "xnxxdi",
        "rfreiv",
        "njbvwj",
        "pkydxy",
        "jksiwj",
        "iaembk",
        "pyqdip",
        "exkykx",
        "uxgecc",
        "khzqgy",
        "dehkbu",
        "ahplng",
        "jomiik",
        "nmcsfe",
        "bclcbp",
        "xfiefi",
        "soiwde",
        "tcjkjp",
        "wervlz",
        "dcthgv",
        "hwwghe",
        "hdlkll",
        "dpzoxb",
        "mpiviy",
        "cprcwo",
        "molttv",
        "dwjtdp",
        "qiilsr",
        "dbnaxs",
        "dbozaw",
        "webcyp",
        "vftnkr",
        "iurlzf",
        "giqcfc",
        "pcghoi",
        "zupyzn",
        "xckegy",
    ]
    Solution().findSecretWord(words, master)
