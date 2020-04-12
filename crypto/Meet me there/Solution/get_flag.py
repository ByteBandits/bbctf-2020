#!/usr/bin/python

from Crypto.Cipher import AES

key1 = 'plug in key1'
key2 = 'plug in key2'
enc_flag = 'plug in encrypted flag'

cipher1 = AES.new(key=key1, mode=AES.MODE_ECB)
cipher2 = AES.new(key=key2, mode=AES.MODE_ECB)

flag = cipher1.decrypt((cipher2.decrypt(enc_flag.decode('hex')).decode('hex'))).decode('hex')