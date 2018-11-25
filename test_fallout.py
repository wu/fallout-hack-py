import unittest

from fallout import WordGame


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.g = WordGame()

    def test_one_word(self):
        self.g.add_word("foo")
        self.g.add_word("bar")
        self.g.add_word("baz")
        self.assertListEqual(self.g.available(), ['foo', 'bar', 'baz'])

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
        self.assertItemsEqual(['aab'], self.g.available())

    def test_pick_best(self):
        self.g.add_word('aaaa')
        self.g.add_word('aacc')
        self.g.add_word('cccc')
        self.assertEqual('aacc', self.g.pick_best_one(), 'best pick of three words')

    def test_pick_best_reverse(self):
        self.g.add_word('cccc')
        self.g.add_word('aacc')
        self.g.add_word('aaaa')
        self.assertEqual('aacc', self.g.pick_best_one(), 'best pick of three words')

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
        self.assertTrue(results[0][1])
        self.assertTrue(results[1][1])
        self.assertTrue(results[2][1])
        self.assertTrue(results[3][1])
        self.assertFalse(results[4][1])

    def test_pick_best(self):
        self.g.add_word('aaaab')
        self.g.add_word('aaaba')
        self.g.add_word('aabaa')
        self.g.add_word('abaaa')
        self.g.add_word('baaaa')
        self.assertEqual('baaaa', self.g.best_pick(4), 'pick most likely to fail')

    def test_get_paths(self):
        self.g.add_word('aab')
        self.g.add_word('aba')
        self.g.add_word('baa')
        self.assertListEqual([[True, 'aab'],
                              [True, 'aba', 'aab'],
                              [True, 'baa', 'aab'],
                              [True, 'aab', 'aba'],
                              [True, 'aba'],
                              [True, 'baa', 'aab', 'aba'],
                              [True, 'aab', 'aba', 'baa'],
                              [True, 'aba', 'baa'],
                              [True, 'baa']
                              ],
                             self.g.get_paths(),
                             'getting all possible paths')


    # question:
    #  what is the next word choice that has the least likelihood of failure?
    #    iterate through every possible target word
    #    iterate through every word as a possible next choice
    #    play every game to completion
    #    find failures
    #    return word that leads to least failures
    #

    # run simulation
    #   iterate through every possible word as the target
    #   attempt to solve the game using best guess
    #   if no failure paths, just use best guess for remaining guesses
    # handle failure paths
    #  if we get here, there is a risk the game will not be won
    #  need to consider which choice that has the least likelihood of failure
    #  identify which choice has the least failure paths


    # new solution
    # - iterate through every possible word to use as the best choice
    # - see which 'best choice' words have no failure paths

    # verify check all words are same length


if __name__ == '__main__':
    unittest.main()
