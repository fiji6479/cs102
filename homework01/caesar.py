import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in list(plaintext):

        if i.isalpha():

            if i.isupper():
                ascii_code = ord(i) + shift
                if ascii_code >= 91:
                    ascii_code = (ascii_code - 90) + 64
                ciphertext += chr(ascii_code)
            else:
                ascii_code = ord(i) + shift
                if ascii_code >= 123:
                    ascii_code = (ascii_code - 122) + 96
                ciphertext += chr(ascii_code)
        else:
            ciphertext += i

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in list(ciphertext):
        if i.isalpha():
            if i.isupper():
                ascii_code = ord(i) - shift
                if ascii_code <= 64:
                    ascii_code = 91 - (65 - ascii_code)
                plaintext += chr(ascii_code)
            else:
                ascii_code = ord(i) - shift
                if ascii_code <= 96:
                    ascii_code = 123 - (97 - ascii_code)
                plaintext += chr(ascii_code)
        else:
            plaintext += i
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
