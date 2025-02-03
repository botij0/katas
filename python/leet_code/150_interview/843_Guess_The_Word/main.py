import random


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
        i = 0
        tries = 0
        coincidence_word = ""
        current_secret = {0: "", 1: "", 2: "", 3: "", 4: "", 5: ""}
        max_coincidence = 0
        bad_letters = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
        for word in random.sample(words, len(words)):
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
                current_secret,
            )

            if max_coincidence == 6:
                print(
                    "You guessed the secret word correctly. Secret word is",
                    coincidence_word,
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
        current_secret: dict,
    ):
        if self.should_try_new_word(
            word, coincidence_word, max_coincidence, bad_letters, current_secret
        ):
            current_coincidences = master.guess(word)
            tries += 1
            print(word, coincidence_word, tries, max_coincidence, current_coincidences)

            if current_coincidences == 0:
                self.update_bad_letters(coincidence_word, word, bad_letters)
                self.clean_current_secret(word, current_secret)

            if max_coincidence != 0 and current_coincidences == max_coincidence:
                self.update_current_secret(word, coincidence_word, current_secret)
                if max_coincidence == 1:
                    print(current_secret)
                    if self.validate_secret(current_secret, master) is False:
                        print("not validddddddd")
                        self.clean_current_secret(word, current_secret)
                    print(current_secret)
                    tries += 1

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
        current_secret: dict,
    ):
        if self.check_current_secret(word, current_secret):
            return False
        if self.check_bad_letters(word, bad_letters):
            return False
        if not self.check_same_coincidences(coincidence_word, word, max_coincidences):
            return False
        return True

    def check_current_secret(self, word: str, current_secret: dict) -> bool:
        print(word, current_secret)
        for i in range(len(word)):
            if current_secret[i] != "":
                if word[i] != current_secret[i]:
                    return True
        return False

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

    def update_current_secret(
        self, word: str, coincidence_word: str, current_secret: dict
    ):
        for i in range(len(word)):
            if word[i] == coincidence_word[i]:
                current_secret[i] = word[i]

    def clean_current_secret(self, word: str, current_secret: dict):
        for i in range(len(word)):
            if word[i] == current_secret[i]:
                current_secret[i] = ""

    def validate_secret(self, current_secret: dict, master):
        secret_try = ""
        for val in current_secret.values():
            if val != "":
                secret_try += val
            else:
                secret_try += "*"

        aux = master.guess(secret_try)
        print(secret_try, aux)
        if aux >= 1:
            return True
        else:
            return False


if __name__ == "__main__":
    master = Master("anqomr", 11)
    words = [
        "pzrooh",
        "aaakrw",
        "vgvkxb",
        "ilaumf",
        "snzsrz",
        "qymapx",
        "hhjgwz",
        "mymxyu",
        "jglmrs",
        "yycsvl",
        "fuyzco",
        "ivfyfx",
        "hzlhqt",
        "ansstc",
        "ujkfnr",
        "jrekmp",
        "himbkv",
        "tjztqw",
        "jmcapu",
        "gwwwmd",
        "ffpond",
        "ytzssw",
        "afyjnp",
        "ttrfzi",
        "xkwmsz",
        "oavtsf",
        "krwjwb",
        "bkgjcs",
        "vsigmc",
        "qhpxxt",
        "apzrtt",
        "posjnv",
        "zlatkz",
        "zynlqc",
        "czajmi",
        "smmbhm",
        "rvlxav",
        "wkytta",
        "dzkfer",
        "urajfh",
        "lsroct",
        "gihvuu",
        "qtnlhu",
        "ucjgio",
        "xyycvd",
        "fsssoo",
        "kdtmux",
        "bxnppe",
        "usucra",
        "hvsmau",
        "gstvvg",
        "ypueay",
        "qdlvod",
        "djfbgs",
        "mcufib",
        "prohkc",
        "dsqgms",
        "eoasya",
        "kzplbv",
        "rcuevr",
        "iwapqf",
        "ucqdac",
        "anqomr",
        "msztnf",
        "tppefv",
        "mplbgz",
        "xnskvo",
        "euhxrh",
        "xrqxzw",
        "wraxvn",
        "zjhlou",
        "xwdvvl",
        "dkbiys",
        "zbtnuv",
        "gxrhjh",
        "ctrczk",
        "iwylwn",
        "wefuhr",
        "enlcrg",
        "eimtep",
        "xzvntq",
        "zvygyf",
        "tbzmzk",
        "xjptby",
        "uxyacb",
        "mbalze",
        "bjosah",
        "ckojzr",
        "ihboso",
        "ogxylw",
        "cfnatk",
        "zijwnl",
        "eczmmc",
        "uazfyo",
        "apywnl",
        "jiraqa",
        "yjksyd",
        "mrpczo",
        "qqmhnb",
        "xxvsbx",
    ]
    Solution().findSecretWord(words, master)
