import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import DES3

class DESCipher(object):

    def __init__(self, key): 
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()
        self.key = self.key[16:]

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(DES3.block_size)
        cipher = DES3.new(self.key, DES3.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:DES3.block_size]
        cipher = DES3.new(self.key, DES3.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[DES3.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs).encode('utf-8')

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]