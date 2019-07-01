from Crypto.Cipher import AES
import hashlib

def pad(text):
    while len(text) % 16 != 0:
        text += '0'
    return text

ct=open('cipher','rb')
key=open('keycbc','r')

cipher = AES.new(str(key.read()).encode("utf8"), AES.MODE_CBC, '1111111111111111'.encode("utf8"))
ciphertext=ct.read()
text = cipher.decrypt(ciphertext)
print(text)
