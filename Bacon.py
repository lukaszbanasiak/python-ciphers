from unicodedata import normalize
import optparse
import codecs
import sys
import re

__author__ = 'Lukasz Banasiak <lukasz@banasiak.me>'
__version__ = '1.0'


def generate_dict():

    """
    Create Bacon dictionary.

    a   AAAAA   g     AABBA   n    ABBAA   t     BAABA
    b   AAAAB   h     AABBB   o    ABBAB   u-v   BAABB
    c   AAABA   i-j   ABAAA   p    ABBBA   w     BABAA
    d   AAABB   k     ABAAB   q    ABBBB   x     BABAB
    e   AABAA   l     ABABA   r    BAAAA   y     BABBA
    f   AABAB   m     ABABB   s    BAAAB   z     BABBB

    :return: Bacon dict
    """

    bacon_dict = {}

    for i in xrange(0, 26):
        tmp = bin(i)[2:].zfill(5)
        tmp = tmp.replace('0', 'a')
        tmp = tmp.replace('1', 'b')
        bacon_dict[tmp] = chr(65 + i)

    return bacon_dict


def encode(words, bacon_dict):

    """
    Encrypt text to Bacon's cipher.

    :param words: string to encrypt
    :param bacon_dict: Bacon dict
    :return: encrypted string
    """

    cipher = ''
    bacon_dict = {v: k for k, v in bacon_dict.items()}  # hack to get key from value - reverse dict
    words = normalize('NFKD', words).encode('ascii', 'ignore')  # replace national characters to ASCII equivalents
    words = words.upper()
    words = re.sub(r'[^A-Z]+', '', words)

    for i in words:
            cipher += bacon_dict.get(i).upper()
    return cipher


def decode(words, bacon_dict):

    """
    Decrypt Bacon's cipher to text.

    :param words: string to decrypt
    :param bacon_dict: Bacon dict
    :return: decrypted string
    """

    cipher = ''
    words = words.lower()
    words = re.sub(r'[^ab]+', '', words)

    for i in xrange(0, len(words) / 5):
        cipher += bacon_dict.get(words[i * 5:i * 5 + 5], ' ')
    return cipher


if __name__ == '__main__':
    parser = optparse.OptionParser(version=__version__)
    parser.set_usage(sys.argv[0] + ' [option]')

    parser.add_option('-d', dest='decrypt', action='store_true', default=False,
                      help='tryb deszyfrowania')
    parser.add_option('-f', dest='file', action='store', default=False,
                      help='wskaz plik z tekstem do (de)szyfrowania')

    (options, args) = parser.parse_args()

    print ''
    print 'Szyfr Bacona'
    print ''
    print '       Autor: ' + __author__

    if options.decrypt:
        print '        Tryb: Deszyfrowanie'
    else:
        print '        Tryb: Szyfrowanie'

    bacon_dict = generate_dict()

    if options.file:
        print ''
        print ' IN> ' + options.file

        try:
            file_stream = codecs.open(options.file, 'r', 'dbcs')
            file_output = codecs.open('_' + options.file, 'w', 'dbcs')
            for line in file_stream:
                if options.decrypt:
                    file_output.write(decode(line, bacon_dict))
                else:
                    file_output.write(encode(line, bacon_dict))
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
                    print 'OUT> ' + decode(text, bacon_dict)
                else:
                    print 'OUT> ' + encode(text, bacon_dict)
            except (SystemExit, KeyboardInterrupt):
                sys.exit(0)