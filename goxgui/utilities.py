import base64
import hashlib
import binascii
from Crypto.Cipher import AES
import sys
import os
import platform


platform_string = None


def encrypt(secret, password):
    '''
    Encrypts the specified secret using the specified password.
    '''

    # pylint: disable=E1101
    hashed_pass = hashlib.sha512(password.encode('utf-8')).digest()
    crypt_key = hashed_pass[:32]
    crypt_ini = hashed_pass[-16:]
    aes = AES.new(crypt_key, AES.MODE_OFB, crypt_ini)

    # since the secret is a base64 string we can just just pad it with
    # spaces which can easily be stripped again after decryping
  