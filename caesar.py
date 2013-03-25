# -*- coding: utf-8 -*-
__author__ = 'Lukasz Banasiak <lukasz@banasiak.me>'

pl_lo = list('aąbcćdeęfghijklłmnńoóprsśtuwyzźż')
pl_up = list('AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ')

en_lo = list('abcdefghijklmnopqrstuvwxyz')
en_up = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def caesar_cipher_pl(words, shift):
    cipher = ''

    for word in words:
        if not (word in pl_lo or word in pl_up):
            cipher += word
        else:
            if word in pl_lo:
                cipher += pl_lo[(pl_lo.index(word) + shift) % len(pl_lo)]
            else:
                cipher += pl_up[(pl_up.index(word) + shift) % len(pl_up)]
    return cipher

def caesar_cipher_en(data, shift):
    cipher = ''
    for d in data:
        if (ord(d) > 64) and (ord(d) < 88) or (ord(d) > 96) and (ord(d) < 120):
            d = chr((ord(d) + shift) % 256)
        elif (ord(d) > 87) and (ord(d) < 91) or (ord(d) > 119) and (ord(d) < 123):
            d = chr(((ord(d) + shift) - 26) % 256)
        cipher += d
    return cipher

if __name__ == '__main__':
    text = raw_input(' IN> ')
    print 'OUT> ' + caesar_cipher_pl(text, 3)