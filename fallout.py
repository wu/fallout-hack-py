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

        # rint("best: " + max_word + " [" + str(max_score) + "]")
        return max_word

    def simulate_one(self, word, turns):
        # print("\nsimulation")
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
                # print("successfully guessed: " + word)
                success = True
                break

        self.words = savewords
        self.guesses = saveguesses

        return [guesses, success, word]

    def simulate_all(self, turns):
        print("\n\nsimulate all")
        results = []
        for word in self.words:
            result = self.simulate_one(word, turns)
            print("simulation results for: " + word + " = " + str(result[1]))
            results.append(result)
        return results


    def best_pick(self, turns):

        max_score = 0
        max_word = ''

        word_scores = {}
        for result in self.simulate_all(turns):
            status = result[1]
            word = result[2]

            if result[1] == True:
                continue

            if word in word_scores:
                word_scores[word] += 1
            else:
                word_scores[word] = 1

            if word_scores[word] > max_score:
                print("New found word: " + word)
                max_score = word_scores[word]
                max_word = word

        print(word_scores)

        return max_word

    def get_paths(self):
        paths = []

        for target in self.words:
            print("target: " + target)

            for idx1 in range(0, len(self.words)):
                word1 = self.words[idx1]

                if word1 == target:
                    paths.append([True, word1])
                    print(word1)
                else:
                    for idx2 in range(0, len(self.words)):
                        word2 = self.words[idx2]
                        if word2 == word1:
                            pass
                        elif word2 == target:
                            paths.append([True, word1, word2])
                            print(word1, word2)
                        else:
                            for idx3 in range(idx2 + 1, len(self.words)):
                                word3 = self.words[idx3]
                                if word3 == word1 or word3 == word2:
                                    pass
                                elif word3 == target:
                                    paths.append([True, word1, word2, word3])
                                    print(word1, word2, word3)
                                else:
                                    for idx4 in range(idx3 + 1, len(self.words)):
                                        word4 = self.words[idx4]
                                        if word4 == word1 or word4 == word2 or word4 == word3:
                                            pass
                                        elif word4 == target:
                                            paths.append([True, word1, word2, word3, word4])
                                            print(word1, word2, word3, word4)
                                        else:
                                            paths.append([False, word1, word2, word3, word4])
                                            print("failure")

        print("paths:")
        for path in paths:
            print(path)

        return paths

