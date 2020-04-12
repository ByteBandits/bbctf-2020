#!/usr/bin/env python3

from flag import flag
from Crypto.Util.number import getPrime
from Crypto.PublicKey import RSA
from base64 import b64encode, b64decode
import os
import multiprocessing
import time

def decrypt(keys, ciphertext):
	from Crypto.Cipher import PKCS1_OAEP
	encryptor = PKCS1_OAEP.new(keys)
	return encryptor.decrypt(ciphertext)

def encrypt(keys, plaintext):
	from Crypto.Cipher import PKCS1_OAEP
	encryptor = PKCS1_OAEP.new(keys)
	return encryptor.encrypt(plaintext)

def gen_rsa_key(bits):
	keys = RSA.generate(bits)
	return keys

def func(bits):
	keys = gen_rsa_key(bits)
	p = keys.p
	q = keys.q
	m = getPrime(bits+1)
	x = pow(p, m, m)*pow(q, m, m) + p*pow(q, m, m) + q*pow(p, m, m) + p*q + pow(p, m-1, m)*pow(q, m-1, m)
	text = os.urandom(32)
	print('Plaintext (b64encoded) : ', b64encode(text).decode())
	print()
	print(hex(x)[2:])
	print(hex(m)[2:])
	# print(b64encode(encrypt(keys, text)))
	print()
	ciphertext = input('Ciphertext (b64encoded) : ')
	ciphertext = b64decode(ciphertext)
	print()
	try:
		plain = decrypt(keys, ciphertext)
	except:
		print("No flag for you !!!")
		exit(0)
	if(plain != text):
		print("No flag for you !!!")
		exit(0)

def main():
	print()
	print("!!! Welcome !!!")
	print("Can you encrypt some data for me :)")
	print()
	for i in range(1024, 1280, 8):
		func(i)
		print()
	print("Flag : ", flag)

if(__name__ == '__main__'):
	main()