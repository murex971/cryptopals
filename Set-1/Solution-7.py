from Crypto.Cipher import AES
from base64 import b64decode

object = AES.new("YELLOW SUBMARINE", AES.MODE_ECB)

ciphertext = b64decode((open("7.txt").read()))
print(object.decrypt(ciphertext))
