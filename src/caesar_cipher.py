# This needs more work to be better converted so it can be used more efficiently by our flask app
from typing import List


def caesar_encipher(shift, message):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    alphabet_code: List[int] = [ord(c) - 97 for c in alphabet]

    cipher_code = [(i - int(shift)) % 26 for i in alphabet_code]

    # strip the whitespace and shift to lowercase.
    formatted_text: str = ""
    for c in message:
        if c not in alphabet and c.lower() not in alphabet:
            continue
        else:
            formatted_text += c.lower()

    cipher = ""
    return cipher.join([chr(cipher_code.index(ord(c) - 97) + 97) for c in formatted_text])
