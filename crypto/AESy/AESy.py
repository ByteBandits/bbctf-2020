#!/usr/bin/python

from Crypto.Cipher import AES
from os import urandom
from string import hexdigits

with open("flag.txt") as f:
    flag = f.read().strip()


KEY = urandom(16)
BLOCK_LEN = 16

def encode_and_pad_message(pt):
    encoded_pt = pt.encode('hex')
    val = BLOCK_LEN - (len(encoded_pt) % BLOCK_LEN)
    return encoded_pt + chr(val)*val 

def encrypt(encoded_pt, key):
    IV = urandom(16)
    cipher = AES.new(key=key, mode=AES.MODE_CBC, iv=IV)
    cipher_text = cipher.encrypt(encoded_pt)

    return (IV + cipher_text).encode('hex')

def decrypt(encoded_ct, key):
    if not len(encoded_ct) % (2*BLOCK_LEN) == 0:
        return "\nAlice: Ciphertext length is not a multiple of block length(=16)."

    if len(encoded_ct) == 32:
        return "\nAlice: You have just given me the IV. There is no encrypted message appended to it??"

    for i in encoded_ct:
        if i not in hexdigits:
            return '\nAlice: There are non-hex digits in the ciphertext.'

    IV = encoded_ct[:32].decode('hex')
    cipher = AES.new(key=key, mode=AES.MODE_CBC, iv=IV)
    ct = encoded_ct[32:].decode('hex')
    padded_pt = cipher.decrypt(ct)

    # print padded_pt.encode('hex')
    pad_byte = padded_pt[-1]
    pad_byte_val = ord(pad_byte)

    if pad_byte_val > BLOCK_LEN or pad_byte_val == 0:
        return "\nAlice: Got your message..??"

    if not padded_pt[-pad_byte_val:] == pad_byte*pad_byte_val:
        return "\nAlice: Got your message..??"

    # pt = padded_pt[:-pad_byte_val]

    return "\nAlice: Got your message!!"

def main():

    print "\nWELCOME TO ALICE's ENCRYPTION SERVICE\n(Plaintext is hex-encoded before encryption)"
    
    while True:
        print "\n"
        print "1. Get your message encrypted."
        print "2. Leave a message for Alice to decrypt."
        print "3. Get Encrypted Flag."
        print "4. Exit."
        print "Enter your choice:"
        choice = raw_input()

        if choice == '1':
            print "\nEnter your message(plaintext):"
            pt = raw_input()
            print "\nHere is your ciphertext(hex-encoded):"
            print encrypt(encode_and_pad_message(pt), KEY)

        elif choice == '2':
            print "\nEnter the ciphertext(hex-encoded):"
            encoded_ct = raw_input()
            print decrypt(encoded_ct, KEY)

        elif choice == '3':
            print "\nHere is your ciphertext(hex-encoded):"
            print encrypt(encode_and_pad_message(flag), KEY)

        else:
            exit()

if __name__ == '__main__':
    main()