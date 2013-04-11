# -*- coding: utf-8 -*-
import optparse
import codecs
import sys

__author__ = 'Lukasz Banasiak <lukasz@banasiak.me>'


def caesar(words, shift, lang='en'):
    """Caesar cipher.

    Simplest and most widely known encryption techniques.

    :param words: string to encrypt
    :param shift: number to rotate
    :param lang: set alphabet to use. EN or PL
    :return: encrypted string
    """

    if 'pl' in lang.lower():
        alphabet = list(u'AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ')
    else:
        alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    cipher = ''

    for word in words:
        if not word.upper() in alphabet:
            cipher += word
        else:
            if word in [x.lower() for x in alphabet]:
                cipher += alphabet[(alphabet.index(word.upper()) + shift) % len(alphabet)].lower()
            else:
                cipher += alphabet[(alphabet.index(word) + shift) % len(alphabet)]
    return cipher


if __name__ == '__main__':
    parser = optparse.OptionParser(version='1.0')
    parser.set_usage(sys.argv[0] + ' [option]')

    parser.add_option('-d', dest='decrypt', action='store_true', default=False,
                      help='tryb deszyfrowania')
    parser.add_option('-s', dest='shift', action='store', default=3,
                      help='liczba przesuniecia wzgledem pierwszej litery alfabetu', type="int")
    parser.add_option('-l', dest='lang', action='store', default='en',
                      help='ustawienie kodowania tekstu: "pl" albo "en"')
    parser.add_option('-f', dest='file', action='store', default=False,
                      help='wskaz plik z tekstem do (de)szyfrowania')

    (options, args) = parser.parse_args()

    print ''
    print 'Szyfr Cezara'
    print ''
    print '       Autor: ' + __author__
    print '   Kodowanie: ' + options.lang
    print 'Przesuniecie: ' + str(options.shift)

    if options.decrypt:
        print '        Tryb: Deszyfrowanie'
        options.shift = options.shift.__neg__()
    else:
        print '        Tryb: Szyfrowanie'

    if options.file:
        print ''
        print ' IN> ' + options.file

        try:
            file_stream = codecs.open(options.file, 'r', 'dbcs')
            file_output = codecs.open('_' + options.file, 'w', 'dbcs')
            for line in file_stream:
                file_output.write(caesar(line, options.shift, lang=options.lang))
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
                print 'OUT> ' + caesar(text, options.shift, lang=options.lang)
            except (SystemExit, KeyboardInterrupt):
                sys.exit(0)