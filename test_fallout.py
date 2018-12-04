import unittest

from fallout import WordGame


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.g = WordGame()

    def test_one_word(self):
        self.g.add_word("foo")
        self.g.add_word("bar")
        self.g.add_word("baz")
        self.assertListEqual(self.g.words, ['foo', 'bar', 'baz'])

    def test_letters_in_common(self):
        self.assertEqual(0, self.g.common_letters('aaa', 'bbb'), 'no common letters')
        self.assertEqual(1, self.g.common_letters('aaa', 'abb'), 'one common letter')
        self.assertEqual(2, self.g.common_letters('aaa', 'aab'), 'two common letter')
        self.assertEqual(3, self.g.common_letters('aaa', 'aaa'), 'all common letters')

    def test_all_available(self):
        self.g.add_word("aaa")
        self.g.add_word("aab")
        self.g.add_word("ccc")
        self.g.add_match('aaa', 2)
        self.assertItemsEqual(['aab'], self.g.words)

    def test_pick_best_one(self):
        self.g.add_word('aaaa')
        self.g.add_word('aacc')
        self.g.add_word('cccc')
        self.assertEqual('aacc', self.g.pick_best_score(), 'best pick of three words')

    def test_pick_best_one_reverse(self):
        self.g.add_word('cccc')
        self.g.add_word('aacc')
        self.g.add_word('aaaa')
        self.assertEqual('aacc', self.g.pick_best_score(), 'best pick of three words')

    def test_simulate_one(self):
        self.g.add_word('aaa')
        self.g.add_word('aac')
        self.g.add_word('ccc')
        self.assertListEqual([['aac', 'ccc'], True, 'ccc'],
                             self.g.simulate_one('ccc', 4)
                             )

    def test_simulate_all(self):
        self.g.add_word('aaa')
        self.g.add_word('aac')
        self.g.add_word('ccc')
        self.assertListEqual([[['aac', 'aaa'], True, 'aaa'],
                              [['aac'], True, 'aac'],
                              [['aac', 'ccc'], True, 'ccc']
                              ],
                             self.g.simulate_all(4)
                             )

    def test_simulate_all_true(self):
        self.g.add_word('aaaab')
        self.g.add_word('aaaba')
        self.g.add_word('aabaa')
        self.g.add_word('abaaa')
        self.g.add_word('baaaa')
        results = self.g.simulate_all(4)
        self.assertListEqual([[['aaaab'], True, 'aaaab'],
                              [['aaaab', 'aaaba'], True, 'aaaba'],
                              [['aaaab', 'aaaba', 'aabaa'], True, 'aabaa'],
                              [['aaaab', 'aaaba', 'aabaa', 'abaaa'], True, 'abaaa'],
                              [['aaaab', 'aaaba', 'aabaa', 'abaaa'], False, 'baaaa'],
                              ],
                             results)

    def test_solver_actual_cases(self):
        cases = self.get_cases()
        total_guesses = 0
        for case in cases:
            g = WordGame()
            answer = case[0]
            words = case[1:]

            for word in words:
                g.add_word(word)
            result = g.solver(answer)
            self.assertTrue(result, 'solver was successful')

            # count total number of guesses on successful guess
            if result:
                total_guesses += result

        self.assertEqual(116, total_guesses, 'solved actual tests in expected guesses')


    def test_solver_best_case(self):
        cases = self.get_cases()
        total_guesses = 0
        for case in cases:
            g = WordGame()
            answer = case[0]
            words = case[1:]

            # move answer to beginning of list to make guessing easier
            words.remove(answer)
            words.insert(0, answer)

            for word in words:
                g.add_word(word)
            result = g.solver(answer)
            self.assertTrue(result, 'solver was successful')

            # count total number of guesses on successful guess
            if result:
                total_guesses += result

        self.assertEqual(99, total_guesses, 'solved best cases in expected guesses')

    def test_solver_worst_case(self):
        cases = self.get_cases()
        total_guesses = 0
        for case in cases:
            g = WordGame()
            answer = case[0]
            words = case[1:]

            # move answer to end of the list to make guessing more difficult
            words.remove(answer)
            words.append(answer)

            for word in words:
                g.add_word(word)
            result = g.solver(answer)
            self.assertTrue(result, 'solver was successful')

            # count total number of guesses on successful guess
            if result:
                total_guesses += result

        self.assertEqual(132, total_guesses, 'solved worst case in expected guesses')

    # verify check all words are same length
    # load test cases
    # generate test cases

    def get_cases(self):
        cases = [
            ["silver", "fierce", "pleads", "insane", "shiner", "wagons", "ripped", "visage", "crimes", "silver", "tables", "wastes"],
            ["cult", "cult", "kind", "bill", "warm", "pare", "good", "loud", "labs", "furs", "pots", "boss"],
            ["take", "self", "atop", "join", "shot", "four", "once", "ways", "take", "hair", "mood", "mace"],
            ["lamp", "dens", "flat", "pays", "full", "farm", "lamp", "colt", "chip", "crap", "cain", "call"],
            ["scene", "scene", "start", "minds", "flame", "types", "while", "aware", "alien", "fails", "wires", "sizes"],
            ["instore", "fanatic", "objects", "instore", "warning", "welfare", "offense", "takings", "stunned", "becomes", "invaded", "decried"],
            ["four", "ball", "call", "cape", "colt", "does", "evil", "face", "four", "hope", "owed", "pots"],
            ["spokes", "across", "devoid", "handle", "herald", "jacket", "marked", "movies", "random", "rather", "refuse", "spokes"],
            ["silks", "allow", "silks", "rolls", "comes", "wires", "sever", "haven", "again", "clear", "paper", "pulls"],
            ["because", "cleared", "allowed", "thieves", "because", "greeted", "between", "stained", "watched", "streets", "country", "dwindle"],
            ["gift", "gift", "iron", "last", "lots", "mood", "nice", "none", "oily", "seat", "shop", "spin"],
            ["wants", "spies", "robes", "dress", "wants", "james", "posed", "rates", "radio", "ready", "sells", "tires"],
            ["fall", "pray", "task", "raid", "lamp", "maul", "fall", "cave", "wave", "rats", "pays", "lays"],
            ["speed", "death", "orbit", "usual", "joins", "broke", "level", "scope", "would", "speed", "scent", "weird"],
            ["waves", "butch", "clock", "hatch", "kinds", "lance", "peace", "ranks", "rubes", "scant", "skins", "waves"],
            ["trip", "hand", "send", "dens", "task", "trip", "went", "says", "beam", "cold", "soap", "none"],
            ["elders", "remain", "armies", "result", "almost", "taurus", "rescue", "failed", "timers", "report", "knight", "elders"],
            ["round", "above", "booty", "round", "voice", "large", "thick", "taint", "scarf", "crude", "ready", "shops"],
            ["poised", "befell", "utmost", "slight", "mongol", "poised", "locals", "ripped", "single", "ritual", "result", "couple"],
            ["sides", "range", "waves", "owned", "raids", "sides", "stead", "races", "raise", "state", "owner", "hired"],
            ["dropped", "dropped", "captain", "routing", "ceiling", "packing", "closest", "fertile", "helping", "caliber", "founded", "desired"],
            ["past", "past", "lays", "huts", "walk", "camp", "sash", "line", "role", "last", "garl", "dais"],
            ["plan", "huts", "hear", "wear", "fork", "very", "loan", "feat", "pack", "rank", "plan", "away", "food"],
            ["cast", "fuse", "fork", "cast", "rule", "tall", "soil", "felt", "rank", "fuel", "here", "tarp"],
            ["vast", "deed", "read", "rush", "sash", "rats", "dead", "also", "owed", "vast", "held", "sets"],
            ["does", "very", "well", "wars", "does", "fork", "huts", "fell", "fear", "cool", "term", "fury"],
            ["exit", "sung", "stay", "exit", "weak", "spin", "yeah", "wish", "step", "star", "mass", "seen"],
            ["hearts", "hearts", "travel", "blamed", "paying", "dapper", "beaten", "passes", "caring", "healed", "wealth", "worked"],
            ["ripper", "teevee", "driver", "thinks", "shiner", "temple", "status", "ripper", "common", "spoils", "center", "yields"],
            ["vipers", "vipers", "justin", "mirror", "wooden", "hauled", "bundle", "street", "failed", "misers", "anyone", "erupts"],
            ["ages", "gang", "ages", "deep", "gain", "none", "nice", "lift", "owns", "lose", "seem", "salt"],
            ["befell", "shovel", "minute", "bowels", "raider", "prayer", "seemed", "oxygen", "module", "single", "befell", "debate"],
            ["tore", "foul", "four", "egos", "tore", "goes", "fell", "join", "golf", "core", "song", "soul"],
            ["seems", "aways", "taunt", "plush", "alert", "loose", "looks", "gangs", "takes", "seems", "scene", "logic"],
            ["section", "dragons", "staying", "hurting", "parties", "winning", "reached", "captain", "outcast", "signals", "section", "reading"],
            ["godfather", "radiation", "crumbling", "engineers", "projector", "surviving", "defensive", "discovery", "godfather", "monocolor", "situation", "murderous"],
            ["same", "died", "hits", "wars", "furs", "fork", "goes", "walk", "used", "holy", "same", "part"],
            ["chooses", "reduced", "shelter", "thrower", "worried", "tonight", "erected", "strange", "turrets", "chooses", "hundred", "godlike"],
            ["armor", "thugs", "notes", "cache", "board", "truth", "shady", "armor", "games", "slips", "speed", "catch"],
            ["retreated", "sponsored", "increased", "processor", "violently", "wastelord", "clockwork", "secretive", "kidnapped", "delimiter", "retreated", "desperate"],
            ["expose", "riches", "cattle", "limped", "figure", "rocket", "expose", "caught", "immune", "gained", "listed", "rifles"],
            ["village", "greatly", "shotgun", "winning", "crushed", "ghengis", "mirrors", "sterile", "insults", "message", "involve", "village"],
        ]
        return cases



if __name__ == '__main__':
    unittest.main()
