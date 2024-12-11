def decrypt(ciphertext, private_key):
    d, n = private_key
    plaintext = ''.join(chr(pow(char, d, n)) for char in ciphertext)
    return plaintext