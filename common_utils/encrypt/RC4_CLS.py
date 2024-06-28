# -*- coding:utf-8 -*-
import random, binascii, base64
from hashlib import sha1


class Rc4(object):

    def __init__(self, secret_key=''):
        self.secret_key = secret_key.lower() or 'chpop5ju9z5jvwdwy5syyg'
        self.salt_length = len(self.secret_key)

    def crypt(self, data, key):
        """RC4 algorithm"""
        x = 0
        box = list(range(256))
        for i in range(256):
            x = (x + int(box[i]) + int(key[i % len(key)])) % 256
            box[i], box[x] = box[x], box[i]
        x = y = 0
        out = []
        for char in data:
            x = (x + 1) % 256
            y = (y + box[x]) % 256
            box[x], box[y] = box[y], box[x]
            out.append(chr(ord(char) ^ box[(box[x] + box[y]) % 256]))
        return ''.join(out)

    def encrypt(self, plaintext:str):
        """RC4 encryption with random salt and final encoding"""
        if not isinstance(plaintext, str):
            raise ValueError
        salt = ''
        for n in range(self.salt_length):
            salt += chr(random.randrange(256))
        data = salt + self.crypt(plaintext, sha1((self.secret_key + salt).encode()).digest())
        return binascii.b2a_hex(data.encode())

    def decrypt(self, ciphertext:str):
        """解密: 密文"""
        if not isinstance(ciphertext, str):
            raise ValueError('to str!')
        ciphertext = binascii.a2b_hex(ciphertext).decode()
        salt = ciphertext[:self.salt_length]
        return self.crypt(ciphertext[self.salt_length:], sha1((self.secret_key + salt).encode()).digest())

# m = 'niki5566'
# an = 'c2a0c29949c2b80b45683bc291c2a7c3acc38fc3a754c2a81461164f660cc29256c398'
# print(Rc4(secret_key='013BE3D8471B5E473CB6229E7981F243').encrypt(m))
# print(Rc4().decrypt(an))
