class WordGame:

    def __init__(self):
        self.words = []
        self.guesses = []

    def add_word(self, word):
        """Add a word to the list of available words"""
        self.words.append(word)

    def add_match(self, chosen_word, match_score):
        """Record a guess and remove words that are no longer candidates"""
        newwords = []
        for word in self.words:
            if self.common_letters(chosen_word, word) == match_score:
                newwords.append(word)

        self.words = newwords

    def pick_best_score(self):
        """Pick the word to guess based on number of letters in common with other words"""
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

    def create_simulator_instance(self):
        """Create a simulator to play from the current state without altering state"""
        g = WordGame()
        g.words = self.words
        g.guesses = self.guesses
        return g

    def simulate_one(self, word, turns):
        """Use a simulator instance to play the game and see if we are successful"""
        g = self.create_simulator_instance()

        guesses = []
        success = False
        for turn in range(0, turns):

            guess = g.pick_best_score()

            guesses.append(guess)

            match_score = g.common_letters(guess, word)
            g.add_match(guess, match_score)

            if guess == word:
                success = True
                break

        return [guesses, success, word]

    def simulate_all(self, turns):
        """For each word, assume that word is the target, and run the simulator"""
        results = []
        for word in self.words:
            result = self.simulate_one(word, turns)
            results.append(result)
        return results

    def simulator_pick(self, turns):
        """Analyze all possible games and return word with highest rate of success"""
        max_score = 0
        max_word = ''

        word_scores = {}
        for result in self.simulate_all(turns):
            status = result[1]
            if not status:
                continue

            word = result[0][0]
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
            return self.pick_best_score()

    def solver(self, word):
        """Attempt to solve a game with a known answer to evaluate the algorithm"""
        g = self.create_simulator_instance()

        for turn in range(0, 4):
            pick = g.simulator_pick(4 - turn)
            match_score = g.common_letters(pick, word)
            if pick == word:
                return turn + 1
            g.add_match(pick, match_score)

        return False

    @staticmethod
    def common_letters(word1, word2):
        """Given two words, return number of letters in common"""
        match_count = 0
        for idx in range(0, len(word1)):
            if word1[idx] == word2[idx]:
                match_count += 1
        return match_count
