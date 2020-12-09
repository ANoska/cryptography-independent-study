# This needs more work to be converted so it can be used by our flask app
from typing import List

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

alphabet_code: List[int] = [ord(c) - 97 for c in alphabet]


def vigenere_encipher(key, message):
    key_word_length = len(key) - 1

    cipher_text = ""
    incrementer = 0
    for c in message:
        if incrementer >= key_word_length or len(cipher_text) == 0:
            incrementer = 0
        else:
            incrementer += 1

        shift: int = ord(key[incrementer]) - 96
        cipher_text += chr(alphabet_code.index(((ord(c) - 97) + shift) % 26) + 97)

    return cipher_text


def vigenere_decipher(key, cipher):
    key_word_length = len(key) - 1

    plain_text = ""
    incrementer = 0
    for c in cipher:
        if incrementer >= key_word_length or len(plain_text) == 0:
            incrementer = 0
        else:
            incrementer += 1

        shift: int = ord(key[incrementer]) - 96
        plain_text += chr(alphabet_code.index(((ord(c) - 97) - shift) % 26) + 97)

    return plain_text
