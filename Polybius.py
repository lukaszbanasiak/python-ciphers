# -*- coding: utf-8 -*-
from unicodedata import normalize
import optparse
import codecs
import sys
import re

__author__ = 'Lukasz Banasiak <lukasz@banasiak.me>'
__version__ = '1.0'

array = [
    list('ABCDE'),
    list('FGHIK'),
    list('LMNOP'),
    list('QRSTU'),
    list('VWXYZ'),
]


def encode(words):

    """
    Polybius square encryption.

    :param words: string to encrypt
    :return: encrypted string
    """

    cipher = ''

    words = normalize('NFKD', words).encode('ascii', 'ignore')  # replace national characters to ASCII equivalents

    for word in words.upper():
        for i in range(len(array)):
            if word in array[i]:
                oy = str(i + 1)
                ox = str((array[i].index(word) + 1))
                cipher += oy + ox + ' '

    cipher = cipher[:-1]  # delete last space

    return cipher


def decode(numbers):

    """
    Polybius square decryption.

    :param numbers: numbers to decrypt
    :return: decrypted string
    """

    numbers = re.sub(r'[\D]+', '', numbers)  # remove non-digit character

    text = ''

    for number in range(0, len(numbers), 2):
        try:
            oy = int(numbers[number]) - 1
            ox = int(numbers[number + 1]) - 1
            text += array[oy][ox]
        except IndexError:
            pass
        continue

    return text


if __name__ == '__main__':
    parser = optparse.OptionParser(version=__version__)
    parser.set_usage(sys.argv[0] + ' [option]')

    parser.add_option('-d', dest='decrypt', action='store_true', default=False,
                      help='tryb deszyfrowania')
    parser.add_option('-f', dest='file', action='store', default=False,
                      help='wskaz plik z tekstem do (de)szyfrowania')

    (options, args) = parser.parse_args()

    print ''
    print 'Szachownica Polibiusza'
    print ''
    print '       Autor: ' + __author__

    if options.decrypt:
        print '        Tryb: Deszyfrowanie'
    else:
        print '        Tryb: Szyfrowanie'

    if options.file:
        print ''
        print ' IN> ' + options.file

        try:
            file_stream = codecs.open(options.file, 'r', 'dbcs')
            file_output = codecs.open('_' + options.file, 'w', 'dbcs')
            for line in file_stream:
                if options.decrypt:
                    file_output.write(decode(line))
                else:
                    file_output.write(encode(line))
            file_stream.close()
            file_output.close()
        except IOError as e:
            print '\nI/O error({0}): {1}'.format(e.errno, e.strerror)
            sys.exit(1)

        print 'OUT> ' + '_' + options.file

    else:
        while 1:
            print ''
            try:
                text = raw_input(' IN> ').decode(sys.stdin.encoding)
                if options.decrypt:
                    print 'OUT> ' + decode(text)
                else:
                    print 'OUT> ' + encode(text)
            except (SystemExit, KeyboardInterrupt):
                sys.exit(0)