from DESCipher import DESCipher
import base64
import hashlib
class Encrypter:
    def __init__(self, text,key):
        self.text = text
        self.key =  key
    def encrypt_image(self):
        des = DESCipher(self.key)
        cipher = des.encrypt(self.text)
        return cipher

class Decrypter:
    def __init__(self, cipher):
        self.cipher = cipher
    def decrypt_image(self,k):
        key = k
        cipher = self.cipher
        des = DESCipher(key)
        base64_decoded = des.decrypt(cipher)
        fh = open("decryptedImage.png", "wb")
        fh.write(base64.b64decode(base64_decoded))
        fh.close() 
        return (base64.b64decode(base64_decoded))
        

