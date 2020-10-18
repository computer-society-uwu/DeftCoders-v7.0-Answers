import re

sm=input()
sk=input()

def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext

if(re.match(r'^[A-Z]+$',sm) and re.match(r'^[A-Z]+$',sk)):
    if(3<len(sm) and len(sm)<100):
        if(2<len(sk) and len(sk)<10):
            print(decrypt(sm,sk))
