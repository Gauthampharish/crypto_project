# Python
from Crypto.Cipher import AES, DES3, Blowfish
from Crypto.Util.Padding import unpad
import json

class AESdec:
    def __init__(self, key, iv):
        self.key = key # Convert string to bytes
        self.iv = iv

    def decrypt(self, ciphertext):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)

class DES3dec:
    def __init__(self, key, iv):
        self.key = key  # Convert string to bytes
        self.iv = iv

    def decrypt(self, ciphertext):
        cipher = DES3.new(self.key, DES3.MODE_CBC, self.iv)
        return unpad(cipher.decrypt(ciphertext[DES3.block_size:]), DES3.block_size)

class BFishdec:
    def __init__(self, key, iv):
        self.key = key# Convert string to bytes
        self.iv = iv

    def decrypt(self, ciphertext):
        cipher = Blowfish.new(self.key, Blowfish.MODE_CBC, self.iv)
        return unpad(cipher.decrypt(ciphertext[Blowfish.block_size:]), Blowfish.block_size)

# Load the keys and IVs from a file
with open('keys.json', 'r') as f:
    keys = json.load(f)

aes_key = keys['aes']['key']
aes_iv = keys['aes']['iv']

des3_key = keys['des3']['key']
des3_iv = keys['des3']['iv']

bfish_key = keys['bfish']['key']
bfish_iv = keys['bfish']['iv']