#from markov import Markov
import markov

import unittest

class TestMarkov(unittest.TestCase):
    def test_markov(self):
        m = markov.Markov("ab")
        result = m.predict("a")
        self.assertEqual(result, "b")

    def test_get_table(self):
        result = markov.get_table('ab')
        self.assertEqual(result, {'a': {'b': 1}})


if __name__ == '__main__':
    unittest.main()
