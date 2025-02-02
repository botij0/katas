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
        words.sort()
        tries = 0
        coincidence_word = ""
        max_coincidence = 0
        bad_words = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
        for i in range(len(words)):
            if tries >= master.allowedGuesses:
                print("you failed")
                return

            coincidence_word, max_coincidence, tries = self.word_try(
                words[i], master, bad_words, max_coincidence, coincidence_word, tries
            )
            coincidence_word, max_coincidence, tries = self.word_try(
                words[len(words) - i - 1],
                master,
                bad_words,
                max_coincidence,
                coincidence_word,
                tries,
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
        bad_words: dict,
        max_coincidence: int,
        coincidence_word: str,
        tries: int,
    ):
        if self.should_try_new_word(word, coincidence_word, max_coincidence, bad_words):
            x = master.guess(word)
            tries += 1
            print(word, coincidence_word, tries, max_coincidence, x)

            if x == 0:
                if len(coincidence_word) > 0:
                    bad_letters = self.get_bad_letters(coincidence_word, word)
                    for letter in bad_letters:
                        bad_words[letter[0]].append(letter[1])

                else:
                    for i in range(6):
                        bad_words[i].append(word[i])

            if x < max_coincidence:
                coincidence_word = self.modify_coincidenc_word(coincidence_word, word)

            if x == 6:
                return word, x, tries

            if x > max_coincidence:
                max_coincidence = x
                coincidence_word = word

        return coincidence_word, max_coincidence, tries

    def should_try_new_word(
        self, word: str, coincidence_word: str, max_coincidences: int, bad_words: dict
    ):
        bad_letters = 0
        for i, c in enumerate(word):
            if c in bad_words[i]:
                bad_letters += 1

        if bad_letters > 0:
            return False

        coincidences = 0
        for i in range(len(coincidence_word)):
            if coincidence_word[i].isupper():
                if word[i].upper() != coincidence_word[i]:
                    coincidences = -1
                    break
                else:
                    coincidences += 1

            if word[i] == coincidence_word[i]:
                coincidences += 1

        return True if coincidences == max_coincidences else False

    def get_bad_letters(self, coincidence_word: str, word: str):
        bad_letters = []

        for i in range(len(word)):
            if word[i] == coincidence_word[i]:
                bad_letters.append((i, coincidence_word[i]))
        return bad_letters

    def modify_coincidenc_word(self, coincidence_word: str, word: str):
        new_word = list(coincidence_word)

        for i in range(len(word)):
            if word[i] != coincidence_word[i]:
                new_word[i] = coincidence_word[i].capitalize()
        return "".join(new_word)


if __name__ == "__main__":
    master = Master("aaaata", 30)
    words = [
        "aaaaga",
        "aaaaka",
        "aaauaa",
        "aaaaoa",
        "aafaaa",
        "aaaaza",
        "aaaava",
        "agaaaa",
        "aaagaa",
        "aaaaqa",
        "aaaaca",
        "aaaaua",
        "apaaaa",
        "aawaaa",
        "aaaaba",
        "aaaqaa",
        "aayaaa",
        "aaaaja",
        "aaacaa",
        "aaayaa",
        "aaaeaa",
        "aavaaa",
        "aasaaa",
        "aaaapa",
        "aaaaxa",
        "aeaaaa",
        "aaxaaa",
        "akaaaa",
        "aaaoaa",
        "aazaaa",
        "anaaaa",
        "aaaala",
        "aaraaa",
        "aaaata",
        "aaaaia",
        "ajaaaa",
        "aaaaaa",
        "ahaaaa",
        "aaaraa",
        "aaaiaa",
        "aanaaa",
        "alaaaa",
        "aakaaa",
        "aiaaaa",
        "aajaaa",
        "aaakaa",
        "axaaaa",
        "aaqaaa",
        "aaamaa",
        "aapaaa",
        "aaafaa",
        "aaasaa",
        "aadaaa",
        "amaaaa",
        "aaaaea",
        "aabaaa",
        "aaaama",
        "asaaaa",
        "acaaaa",
        "aaiaaa",
        "avaaaa",
        "afaaaa",
        "aoaaaa",
        "aamaaa",
        "aaaasa",
        "aaawaa",
        "azaaaa",
        "aataaa",
        "aaeaaa",
        "aaaafa",
        "aaahaa",
        "aaalaa",
        "aaaana",
        "aaanaa",
        "aaabaa",
        "aaaada",
        "auaaaa",
        "aaapaa",
        "awaaaa",
        "ayaaaa",
        "adaaaa",
        "aaavaa",
        "aagaaa",
        "aauaaa",
        "abaaaa",
        "aaadaa",
        "aqaaaa",
        "aaaxaa",
        "aaaawa",
        "aaajaa",
        "araaaa",
        "aahaaa",
        "aaaaha",
        "aacaaa",
        "aaaara",
        "aaoaaa",
        "ataaaa",
        "aaaaya",
        "aalaaa",
        "aaazaa",
    ]
    Solution().findSecretWord(words, master)
