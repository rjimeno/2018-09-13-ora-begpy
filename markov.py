"""
This is a docstring for the markov module. It is a string
that appears at the top of a Python file.
 
>>> m = Markov('ab')
>>> m.predict('a')
'b'

"""
import random
import urllib.request as req


def fetch_url(url):
    fin = req.urlopen(url)
    return fin.read()


def write_text(txt, filename, enc='utf8'):
    with open(filename, 'w', encoding=enc) as fout:
        fout.write(txt)
    # done, fout will be closed


def get_markov(filename, enc='utf8'):
    with open(filename, encoding=enc) as fin:
        txt = fin.read()
    return Markov(txt)


class Markov:
    def __init__(self, data):
        """This is the constructor docstring"""
        self.table = get_table(data)
 
    def predict(self, data_in):
        options = self.table.get(data_in, {})
        if not options:
            raise KeyError(f"{data_in} not found")
        possibles = []
        for char, count in options.items():
            for i in range(count):
                possibles.append(char)
        # import pdb;pdb.set_trace()
        return random.choice(possibles)


def get_table(data):
    """Function docstring

    >>> get_table('ab')
    {'a': {'b': 1}}
    """
    results = {}
    for i, char in enumerate(data):
        try:
            out = data[i + 1]
        except IndexError:
            break
        char_dict = results.get(char, {})
        char_dict.setdefault(out, 0)
        char_dict[out] += 1
        results[char] = char_dict
    return results
