import base64
import json

from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad, pad

class Cipher:
    def __init__(self, key: str):
        self.cipher = DES.new(key.encode()[:8], DES.MODE_ECB)

    def decrypt(self, ciphertext):
        encrypted_data = base64.b64decode(ciphertext)
        decrypted_data = self.cipher.decrypt(encrypted_data)
        return json.loads(unpad(decrypted_data, self.cipher.block_size))

    def encrypt(self, data):
        encrypted_data = self.cipher.encrypt(pad(json.dumps(data, separators=(',', ':')).encode(), self.cipher.block_size))
        return base64.b64encode(encrypted_data).decode()
