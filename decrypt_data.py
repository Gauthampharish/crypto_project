
import json
from decrypt import AESdec, DES3dec, BFishdec

# Load the keys and IVs from a file

with open('keys.json', 'r') as f:
    keys = json.load(f)

aes_key = bytes.fromhex(keys['aes']['key'])
aes_iv = bytes.fromhex(keys['aes']['iv'])

des3_key = bytes.fromhex(keys['des3']['key'])
des3_iv = bytes.fromhex(keys['des3']['iv'])

bfish_key = bytes.fromhex(keys['bfish']['key'])
bfish_iv = bytes.fromhex(keys['bfish']['iv'])
# Load the encrypted message from a file
with open('encrypted_message.txt', 'rb') as message_file:
    encrypted_message = message_file.read()

# Decrypt the message using Blowfish, then 3DES, then AES
decryption_methods = [BFishdec(bfish_key, bfish_iv), DES3dec(des3_key, des3_iv), AESdec(aes_key, aes_iv)]
decrypted_message = encrypted_message
for method in decryption_methods:
    decrypted_message = method.decrypt(decrypted_message)

print(decrypted_message.decode())