# -*- coding: utf-8 -*-
from unicodedata import normalize
import optparse
import codecs
import sys

__author__ = 'Lukasz Banasiak <lukasz@banasiak.me>'
__version__ = '1.1'


def atbash(words, mode=0):
    """AtBash cipher.

    Atbash is a simple substitution cipher for the Hebrew alphabet.

    :param words: string to encrypt
    :param mode: set alphabet to use.
                 0 for replace diacritic marks
                 1 for EN
                 2 for PL
    :return: encrypted string
    """

    if mode == 1:
        alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    elif mode == 2:
        alphabet = list(u'AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ')
    else:
        alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        words = normalize('NFKD', words).encode('ascii', 'ignore')  # replace national characters to ASCII equivalents

    cipher = ''

    for word in words:
        if not word.upper() in alphabet:
            cipher += word
        else:
            if word in [x.lower() for x in alphabet]:
                cipher += alphabet[len(alphabet) - alphabet.index(word.upper()) - 1 % len(alphabet)].lower()
            else:
                cipher += alphabet[len(alphabet) - alphabet.index(word) - 1 % len(alphabet)]
    return cipher


if __name__ == '__main__':
    parser = optparse.OptionParser(version=__version__,
                                   usage='Usage: %prog [options] [args]',
                                   description='Atbash is a simple substitution cipher for the Hebrew alphabet.')
    parser.add_option('-d', dest='decrypt', action='store_true', default=False,
                      help='tryb deszyfrowania')
    parser.add_option('-l', dest='lang', action='store', default=0,
                      help='''ustawienie kodowania tekstu:\n
                                    0 - zamiana znakow diakrytycznych na ich odpowiedniki\n
                                    1 - kodowanie dla angielskiego alfabetu\n
                                    2 - kodowanie dla polskiego alfabetu''', type='int')
    parser.add_option('-f', dest='file', action='store', default=False,
                      help='wskaz plik z tekstem do (de)szyfrowania')

    (options, args) = parser.parse_args()

    print ''
    print 'Szyfr AtBash'
    print ''
    print '       Autor: ' + __author__

    if options.lang == 1:
        print '   Kodowanie: dla angielskiego alfabetu'
    elif options.lang == 2:
        print '   Kodowanie: dla polskiego alfabetu'
    else:
        print '   Kodowanie: zamiana znakow diakrytycznych na ich odpowiedniki'

    if options.file:
        print ''
        print ' IN> ' + options.file

        try:
            file_stream = codecs.open(options.file, 'r', 'dbcs')
            file_output = codecs.open('_' + options.file, 'w', 'dbcs')
            for line in file_stream:
                file_output.write(atbash(line, mode=options.lang))
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
                print 'OUT> ' + atbash(text, mode=options.lang)
            except (SystemExit, KeyboardInterrupt):
                sys.exit(0)
