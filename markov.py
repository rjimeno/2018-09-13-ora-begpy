#!/usr/bin/env python3

"""
This is a docstring for the markov module. It is a string
that appears at the top of a Python file.
 
>>> m = Markov('ab')
>>> m.predict('a')
'b'

"""
import argparse
import random
import sys
import urllib.request as req


def fetch_url(url):
    fin = req.urlopen(url)
    return fin.read()


def write_text(txt, filename, enc='utf8'):
    with open(filename, 'w', encoding=enc) as fout:
        fout.write(txt)
    # done, fout will be closed


def get_markov(filename, enc='utf8', size=1):
    with open(filename, encoding=enc) as fin:
        txt = fin.read()
    return Markov(txt, size)


def repl(m):
    """This gives you a REPL for a Markov chain."""
    print("Welcome to the REPL. Hit Ctrl-C to exit.")
    while True:
        try:
            txt = input(">")
        except KeyboardInterrupt:
            print("Goodbye!")
            break
        try:
            res = m.predict(txt)
        except KeyError:
            print("Not found.")
        except IndexError:
            print("Whooops. Try again.")
        else:
            print(res)


class Markov:
    def __init__(self, data, size=1):
        """This is the constructor docstring

        >>> m2 = Markov('abc')
        >>> m2.predict('b')
        'c'
        """
        self.tables = []
        for i in range(size):
            self.tables.append(get_table(data, size=i + 1))
        # self.table = get_table(data)

    def predict(self, data_in):
        table = self.tables[len(data_in) - 1]
        options = table.get(data_in, {})
        if not options:
            raise KeyError(f"{data_in} not found")
        possibles = []
        for char, count in options.items():
            for i in range(count):
                possibles.append(char)
        # import pdb;pdb.set_trace()
        return random.choice(possibles)


def get_table(data, size=1):
    """Function docstring

    >>> get_table('ab')
    {'a': {'b': 1}}
    """
    results = {}
    for i, _ in enumerate(data):
        chars = data[i:i + size]
        try:
            out = data[i + size]
        except IndexError:
            break
        char_dict = results.get(chars, {})
        char_dict.setdefault(out, 0)
        char_dict[out] += 1
        results[chars] = char_dict
    return results


def main(args):
    ap = argparse.ArgumentParser()
    ap.add_argument('-f', '--file', help='Input file')
    ap.add_argument('-s', '--size', help='Markov size',
                    default=1, type=int)
    opts = ap.parse_args(args)
    if opts.file:
        m = get_markov(opts.file, size=opts.size)
        repl(m)


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    main(sys.argv[1:])
