# -*- coding: utf-8 -*-
from collections import Counter
from math import log, ceil
from heapq import heappush, heappop, heapify
from unicodedata import normalize as norm
import codecs
import optparse
import re
import sys

__author__ = 'Lukasz Banasiak'
__version__ = '1.1'
__description__ = """In cryptanalysis, frequency analysis is the study
 of the frequency of letters or groups of letters in a ciphertext."""


def national2ascii(data):
    return norm('NFKD', data).encode('ascii', 'ignore')


def huffman(counter):
    heap = [[wt, [sym, ""]] for sym, wt in counter.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


def fi(per, v):
    return per/100 * int(ceil(v))


def hi(per):
    return -log(per/100, 2)


def entropy(per):
    return -(per/100 * log(per/100, 2))


def percentage(p, lns):
    return float(p) / float(lns) * 100


def count(words, all_chars=False, normalize=False):
    """Character frequency analysis.

    A simple analysis of the characters in the text.

    :param words: string to count
    :param all_chars: set counting all characters
    :param normalize: replace national characters to ASCII equivalents
    """

    if normalize:
        words = national2ascii(words)

    regex = re.compile(u'^[a-zA-ZĄĘŚĆŻŹŁÓĆŃąęśćżźłóćń]+$')
    counter = Counter()

    for char in words:
        if not all_chars:
            if regex.match(char):
                counter[char] += 1
        else:
            if not char in ['\r', '\n', u'\u2013']:
                counter[char] += 1
    return counter


def _print(counter):
    H = []
    L = []
    print 'Char\tCount\t\tPercent\tHi\tFi\tHuffman'
    print '-'*70
    for char in huffman(counter):
        per = percentage(counter[char[0]], sum(counter.values()))
        h = entropy(per)
        H.append(h)
        l = fi(per, hi(per))
        L.append(l)
        print '%s\t%d\t\t%.3f%%\t%.3f\t%.3f\t%s' % (char[0], counter[char[0]], per, hi(per), l, char[1])
    print '-'*70
    print '+:\t%s' % sum(counter.values())
    print '='*70
    print 'H: %s' % sum(H)
    print 'L: %s' % sum(L)


if __name__ == '__main__':
    parser = optparse.OptionParser(version=__version__, usage='Usage: %prog [options] [args]',
                                   description=__description__)
    parser.add_option('-a', dest='allchars', action='store_true', default=True, help='count all chars')
    parser.add_option('-c', dest='case_sensitive', action='store_true', default=True, help='case-sensitivity')
    parser.add_option('-n', dest='normalize', action='store_true', default=False,
                      help='replace national characters to ASCII equivalents')
    parser.add_option('-f', dest='file', action='store', default=False, help='text file')

    (options, args) = parser.parse_args()

    print 'Characters Frequency Analysis'
    print 'Author: %s' % __author__
    print 'Count all chars: %s' % options.allchars
    print 'Case-sensitivity: %s' % options.case_sensitive
    print 'Replace national characters to ASCII equivalents: %s' % options.normalize
    print
    if options.file:
        try:
            file_stream = codecs.open(options.file, 'r', 'dbcs')
        except IOError as e:
            print '%s: %s' % (e.strerror, options.file)
        else:
            print '>>> ' + options.file
            text = file_stream.read()
            if not options.case_sensitive:
                text = text.upper()
            _print(count(text, all_chars=options.allchars, normalize=options.normalize))
            file_stream.close()
    else:
        while 1:
            try:
                text = raw_input('>>> ').decode(sys.stdin.encoding)
            except (SystemExit, KeyboardInterrupt) as e:
                sys.exit(0)
            else:
                if not options.case_sensitive:
                    text = text.upper()
                _print(count(text, all_chars=options.allchars, normalize=options.normalize))