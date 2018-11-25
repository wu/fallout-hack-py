class WordGame:

    def __init__(self):
        self.words = []
        self.guesses = []

    def add_word(self, word):
        self.words.append(word)

    def available(self):
        return self.words

    def add_match(self, chosen_word, match_score):
        newwords = []
        for word in self.words:
            if self.common_letters(chosen_word, word) == match_score:
                newwords.append(word)

        self.words = newwords

    def common_letters(self, word1, word2):
        match_count = 0
        for idx in range(0, len(word1)):
            if word1[idx] == word2[idx]:
                match_count += 1
        return match_count

    def pick_best_one(self):
        max_score = 0
        max_word = ''

        for word1 in self.words:
            word1score = 0

            for word2 in self.words:
                word1score += self.common_letters(word1, word2)

            if word1score > max_score:
                max_score = word1score
                max_word = word1

        return max_word

    def simulate_one(self, word, turns):
        savewords = self.words
        saveguesses = self.guesses

        guesses = []
        success = False
        for turn in range(0, turns):

            guess = self.pick_best_one()

            guesses.append(guess)

            match_score = self.common_letters(guess, word)
            self.add_match(guess, match_score)

            if guess == word:
                success = True
                break

        self.words = savewords
        self.guesses = saveguesses

        return [guesses, success, word]

    def simulate_all(self, turns):
        results = []
        for word in self.words:
            result = self.simulate_one(word, turns)
            results.append(result)
        return results

    def best_pick(self, turns):

        max_score = 0
        max_word = ''

        word_scores = {}
        for result in self.simulate_all(turns):
            status = result[1]
            word = result[0][0]

            if result[1] == True:
                continue

            if word in word_scores:
                word_scores[word] += 1
            else:
                word_scores[word] = 1

            if word_scores[word] > max_score:
                max_score = word_scores[word]
                max_word = word

        if max_word:
            return max_word
        else:
            return self.pick_best_one()

    def solver(self, word):
        savewords = self.words
        saveguesses = self.guesses

        for turn in range(0, 4):
            pick = self.best_pick(4 - turn)
            if pick == word:
                self.words = savewords
                self.guesses = saveguesses
                return True
            self.add_match(pick, self.common_letters(pick, word))

        self.words = savewords
        self.guesses = saveguesses

        return False
