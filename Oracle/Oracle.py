from Crypto.Cipher import AES
import hashlib

def pad(text):
    while len(text) % 16 != 0:
        text += '0'
    return text

pt=open('plaintext','r')
ct=open('cipher','wb')
key=open('keycbc','r')

cipher = AES.new(str(key.read()).encode(), AES.MODE_CBC, '1111111111111111'.encode())
plaintext = pt.read()
plaintext = pad(plaintext)
plaintext = str(plaintext).encode()
ciphertext = cipher.encrypt(plaintext)
ct.write(ciphertext)
ct.close()
