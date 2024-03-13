# Python

import json
from encrypt import AESenc, DES3enc, BFishenc

# Load the keys and IVs from a file
with open('keys.json', 'r') as f:
    keys = json.load(f)

aes_key = keys['aes']['key']
aes_iv = keys['aes']['iv']

des3_key = keys['des3']['key']
des3_iv = keys['des3']['iv']

bfish_key = keys['bfish']['key']
bfish_iv = keys['bfish']['iv']

# Get the message to be encrypted
message = "hello how are you".encode()

# Encrypt the message using AES, then 3DES, then Blowfish
encryption_methods = [AESenc(aes_key, aes_iv), DES3enc(des3_key, des3_iv), BFishenc(bfish_key, bfish_iv)]
encrypted_message = message
for method in encryption_methods:
    encrypted_message = method.encrypt(encrypted_message)
print(encrypted_message)
# Write the final encrypted message to a file
with open('encrypted_message.txt', 'wb') as message_file:
    message_file.write(encrypted_message)