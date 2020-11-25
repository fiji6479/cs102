def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
        Encrypts plaintext using a Vigenere cipher.

        >>> encrypt_vigenere("PYTHON", "A")
        'PYTHON'
        >>> encrypt_vigenere("python", "a")
        'python'
        >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
        'LXFOPVEFRNHR'
        """
    ciphertext = ""
    keyword_lower = keyword.lower()
    while len(keyword_lower) < len(plaintext):
        keyword_lower = keyword_lower + keyword_lower

    for j in range(len((plaintext))):
        letter = plaintext[j]
        key = keyword_lower[j]
        shift = ord(key) - 97
        if letter.isupper():

            ascii_code = ord(letter) + shift
            if ascii_code >= 91:
                ascii_code = (ascii_code - 90) + 64
            ciphertext += chr(ascii_code)
        else:
            ascii_code = ord(letter) + shift
            if ascii_code >= 123:
                ascii_code = (ascii_code - 122) + 96
            ciphertext += chr(ascii_code)

    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
        Decrypts a ciphertext using a Vigenere cipher.

        >>> decrypt_vigenere("PYTHON", "A")
        'PYTHON'
        >>> decrypt_vigenere("python", "a")
        'python'
        >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
        'ATTACKATDAWN'
        """
    plaintext = ""
    keyword_lower = keyword.lower()
    while len(keyword_lower) < len(ciphertext):
        keyword_lower = keyword_lower + keyword_lower

    for j in range(len((ciphertext))):
        letter = ciphertext[j]
        key = keyword_lower[j]
        shift = ord(key) - 97
        if letter.isupper():
            ascii_code = ord(letter) - shift
            if ascii_code <= 64:
                ascii_code = 91 - (65 - ascii_code)
            plaintext += chr(ascii_code)
        else:
            ascii_code = ord(letter) - shift
            if ascii_code <= 96:
                ascii_code = 123 - (97 - ascii_code)
            plaintext += chr(ascii_code)

    return plaintext
