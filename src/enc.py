"""
Author: Ali Rizvi (Frontear)
License: GNU GPL 3.0
"""

import zlib
import base64
import hashlib

SEPARATOR = "\0"
ENCODING = "UTF-8"
HASHING = hashlib.blake2b

def encrypt(data: str, key: str) -> bytes:
    arr = []
    data = list(data)
    key_hash = HASHING(key.encode(ENCODING)).hexdigest()

    arr.append(key_hash)

    for i in range(len(data)):
        char, shift = ord(data[i]), ord(key[i % len(key)])
        enc = hex(char + shift)

        arr.append(enc)

    return base64.standard_b64encode(zlib.compress(SEPARATOR.join(arr).encode(ENCODING)))

def decrypt(data: bytes, key: str) -> str:
    arr = []
    data = zlib.decompress(base64.standard_b64decode(data)).decode(ENCODING).split(SEPARATOR)
    key_hash = HASHING(key.encode(ENCODING)).hexdigest()

    if key_hash == data[0]:
        for i in range(len(data := data[1:])):
            char, shift = int(data[i], 16), ord(key[i % len(key)])
            dec = chr(char - shift)

            arr.append(dec)
    else:
        raise InterruptedError("Given password was incorrect. Cannot decrypt")

    return "".join(arr)