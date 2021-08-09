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
    hashed_pass = hashlib.sha512(password.encode('utf