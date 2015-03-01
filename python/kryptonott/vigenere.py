#!/usr/bin/env python3

import itertools
import sys

alphabet = u'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅabcdefghijklmnopqrstuvwxyzæøå .,?-_;:+1234567890"'

def vigenere_encode(msg, key):
    """Function that encodes a string with Vingenere cipher.

    The encrypted string is returned.

    Vigenere kryptering, av Arve Seljebu(arve@seljebu.no),
    MIT License, 2014
    """
    msg_enc = list()
    key_length = len(key)
    alphabet_length = len(alphabet)

    for i,char in enumerate(msg):
        msgInt = alphabet.find(char)
        encInt = alphabet.find(key[i % key_length])

        if msgInt == -1 or encInt == -1:
            return ''

        encoded = (msgInt + encInt) % alphabet_length
        msg_enc.append(alphabet[encoded])

    return ''.join(msg_enc)


def vigenere_decode(msg, key):
    msg_dec = list()
    key_length = len(key)
    alphabet_length = len(alphabet)
    for i, char in enumerate(msg):
        msg_int = alphabet.find(char)
        dec_int = alphabet.find(key[i % key_length])

        if msg_int == -1 or dec_int == -1:
            return ''

        decoded = (msg_int - dec_int) % alphabet_length
        msg_dec.append(alphabet[decoded])

    return ''.join(msg_dec)


def brute_force_attack(secret, key_length, num_spaces):
    key_alphabet = 'insectabdfghjklmopqruvwxyz'
    for key in itertools.product(key_alphabet, repeat=key_length):
        check_key(secret, key, num_spaces)


def dictionary_attack(secret, num_spaces):
    with open('/usr/share/dict/american-english', mode='r') as fid:
        for key in fid:
            check_key(secret, key.strip(), num_spaces)

def check_key(secret, key, num_spaces):
    sentence = vigenere_decode(secret, key)
    if sentence.count(' ') > num_spaces:
        print('{} ({}): {}'.format(key, sentence.count(' '),
                                   sentence))


message = ('It was 79 and the world seemed more kind ... and it was still '
           'OK to be modest')
keyword = 'HipHopFluesopp'

encrypted = vigenere_encode(message, keyword)
decrypted = vigenere_decode(encrypted, keyword)
if decrypted != message:
    print('There is something wrong in the encryption or decryption!')
    print('Original message:  {}'.format(message))
    print('Encrypted message: {}'.format(encrypted))
    print('Decrypted message: {}'.format(decrypted))
    sys.exit(1)


secret = ('q0Ø:;AI"E47FRBQNBG4WNB8B4LQN8ERKC88U8GEN?T6LaNBG4GØ""N6K086HB"'
          'Ø8CRHW"+LS79Ø""N29QCLN5WNEBS8GENBG4FØ47a')
brute_force_attack(secret, 6, 15)

secret = ('t-JO:BK0aM,:CQ+ÆAGW?FJGB0KVCGMQ6SQN"GAIDL-PÅ7954E:7Jr,IÆoCF0M"CQdØ'
          'VlHD53CÅ;IA2DMG5ØHDØVåL:JQØ439LRBBVEMTBÆ6CF0M"CQNAG8G1V6LÅ8FF4Z')
dictionary_attack(secret, 15)
