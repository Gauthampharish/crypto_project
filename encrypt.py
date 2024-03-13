# Python
from Crypto.Cipher import AES, DES3, Blowfish
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import json

class AESenc:
    def __init__(self, key, iv):
        self.key = bytes.fromhex(key)  # Convert hex string to bytes
        self.iv = bytes.fromhex(iv)

    def encrypt(self, message):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return self.iv + cipher.encrypt(pad(message, AES.block_size))

class DES3enc:
    def __init__(self, key, iv):
        self.key = bytes.fromhex(key)  # Convert hex string to bytes
        self.iv = bytes.fromhex(iv)

    def encrypt(self, message):
        cipher = DES3.new(self.key, DES3.MODE_CBC, self.iv)
        return self.iv + cipher.encrypt(pad(message, DES3.block_size))

class BFishenc:
    def __init__(self, key, iv):
        self.key = bytes.fromhex(key)  # Convert hex string to bytes
        self.iv = bytes.fromhex(iv)

    def encrypt(self, message):
        cipher = Blowfish.new(self.key, Blowfish.MODE_CBC, self.iv)
        return self.iv + cipher.encrypt(pad(message, Blowfish.block_size))