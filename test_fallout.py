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

    def test_pick_best_one(self):
        self.g.add_word('aaaa')
        self.g.add_word('aacc')
        self.g.add_word('cccc')
        self.assertEqual('aacc', self.g.pick_best_one(), 'best pick of three words')

    def test_pick_best_one_reverse(self):
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
        self.assertListEqual([[['aaaab'], True, 'aaaab'],
                              [['aaaab', 'aaaba'], True, 'aaaba'],
                              [['aaaab', 'aaaba', 'aabaa'], True, 'aabaa'],
                              [['aaaab', 'aaaba', 'aabaa', 'abaaa'], True, 'abaaa'],
                              [['aaaab', 'aaaba', 'aabaa', 'abaaa'], False, 'baaaa'],
                              ],
                             results)

    # def test_analyze_simulation_results(self):
    #     simulation_results = [[['aaaab'], True, 'aaaab'],
    #                           [['aaaab', 'aaaba'], True, 'aaaba'],
    #                           [['aaaab', 'aaaba', 'aabaa'], True, 'aabaa'],
    #                           [['aaaab', 'aaaba', 'aabaa', 'abaaa'], True, 'abaaa'],
    #                           [['aaaab', 'aaaba', 'aabaa', 'abaaa'], False, 'baaaa'],
    #                           ]

    def test_solver_silver(self):
        self.g.add_word('fierce')
        self.g.add_word('pleads')
        self.g.add_word('insane')
        self.g.add_word('shiner')
        self.g.add_word('wagons')
        self.g.add_word('ripped')
        self.g.add_word('visage')
        self.g.add_word('crimes')
        self.g.add_word('silver')
        self.g.add_word('tables')
        self.g.add_word('wastes')
        self.assertTrue(self.g.solver('silver'), 'running solver')

    def test_solver_cult_first(self):
        self.g.add_word('cult')
        self.g.add_word('kind')
        self.g.add_word('bill')
        self.g.add_word('warm')
        self.g.add_word('pare')
        self.g.add_word('good')
        self.g.add_word('loud')
        self.g.add_word('labs')
        self.g.add_word('furs')
        self.g.add_word('pots')
        self.g.add_word('boss')
        self.assertTrue(self.g.solver('cult'), 'running solver')

    def test_solver_cult_last(self):
        self.g.add_word('kind')
        self.g.add_word('bill')
        self.g.add_word('warm')
        self.g.add_word('pare')
        self.g.add_word('good')
        self.g.add_word('loud')
        self.g.add_word('labs')
        self.g.add_word('furs')
        self.g.add_word('pots')
        self.g.add_word('boss')
        self.g.add_word('cult')
        self.assertTrue(self.g.solver('cult'), 'running solver')

    #
    # def test_pick_best(self):
    #     self.g.add_word('aaaab')
    #     self.g.add_word('aaaba')
    #     self.g.add_word('aabaa')
    #     self.g.add_word('abaaa')
    #     self.g.add_word('baaaa')
    #     self.assertEqual('baaaa', self.g.best_pick(4), 'pick most likely to fail')
    #

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
