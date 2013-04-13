# -*- coding: utf-8 -*-
import Polybius
import optparse
import codecs
import sys
import re

__author__ = 'Lukasz Banasiak <lukasz@banasiak.me>'
__version__ = '1.0'


def transform(data):

    data = re.sub(r'[\D]+', '', data)

    return data[::2] + data[1::2]


def transform_back(data):

    data = re.sub(r'[\D]+', '', data)
    numbers = ''

    a, b = (data[:len(data) / 2], data[len(data) / 2:])

    for i in range(len(a)):
        numbers += a[i] + b[i]

    return numbers


if __name__ == '__main__':
    parser = optparse.OptionParser(version=__version__,
                                   usage='Usage: %prog [options] [args]',
                                   description='Bifid cipher is a cipher which combines the Polybius square with transposition, and uses fractionation to achieve diffusion.')
    parser.add_option('-d', dest='decrypt', action='store_true', default=False,
                      help='tryb deszyfrowania')
    parser.add_option('-k', dest='key', action='store', default='', type='string',
                      help='klucz transformacji szachownicy')
    parser.add_option('-V', dest='verbose', action='store_true', default=False,
                      help='pokazuje posrednie etapy')
    parser.add_option('-f', dest='file', action='store', default=False,
                      help='wskaz plik z tekstem do (de)szyfrowania')

    (options, args) = parser.parse_args()

    print ''
    print 'Szyfr Delastelle\'a'
    print ''
    print '       Autor: ' + __author__

    if options.decrypt:
        print '        Tryb: Deszyfrowanie'
    else:
        print '        Tryb: Szyfrowanie'

    if options.verbose:
        print 'Tryb verbose: Tak'
    else:
        print 'Tryb verbose: Nie'

    array = Polybius.generate_array(key=options.key)

    print ' Szachownica:'
    Polybius.display_array(array)

    if options.file:
        print ''
        print ' IN> ' + options.file

        try:
            file_stream = codecs.open(options.file, 'r', 'dbcs')
            file_output = codecs.open('_' + options.file, 'w', 'dbcs')
            for line in file_stream:
                if options.decrypt:
                    file_output.write(Polybius.decode(
                        transform_back(
                            Polybius.encode(line, array)), array))
                else:
                    file_output.write(Polybius.decode(
                        transform(
                            Polybius.encode(line, array)), array))
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
                    if options.verbose:
                        print '1: %s   # po wyznaczeniu wspolrzednych' % Polybius.format_cipher(
                            Polybius.encode(text, array))
                        print '2: %s   # po transformacji poziomej' % Polybius.format_cipher(
                            transform_back(
                                Polybius.encode(text, array)))
                    print 'OUT> ' + Polybius.decode(
                        transform_back(
                            Polybius.encode(text, array)), array)
                else:
                    if options.verbose:
                        print '1: %s  # po wyznaczeniu wspolrzednych' % Polybius.format_cipher(
                            Polybius.encode(text, array))
                        print '2: %s  # po transformacji poziomej' % Polybius.format_cipher(
                            transform_back(
                                Polybius.encode(text, array)))
                    print 'OUT> ' + Polybius.decode(
                        transform(
                            Polybius.encode(text, array)), array)
            except (SystemExit, KeyboardInterrupt):
                sys.exit(0)