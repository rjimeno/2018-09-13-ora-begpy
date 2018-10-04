from markov import Markov, get_table
# import markov

import unittest


class TestMarkov(unittest.TestCase):
    def test_markov(self):
        m = Markov('ab')
        result = m.predict('a')
        self.assertEqual(result, 'b')

    def test_markov2(self):
        m = Markov('abc', size=2)
        result = m.predict('ab')
        self.assertEqual(result, 'c')

    def test_get_table(self):
        result = get_table('ab')
        self.assertEqual(result, {'a': {'b': 1}})

    def test_get_table2(self):
        result = get_table('abc', size=2)
        self.assertEqual(result, {'ab': {'c': 1}})


if __name__ == '__main__':
    unittest.main()
