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

    # verify check all words are same length
    # load test cases
    # generate test cases


if __name__ == '__main__':
    unittest.main()
