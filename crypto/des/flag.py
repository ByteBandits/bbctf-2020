import os
flag = open('flag.txt').read().encode()
key = os.urandom(1024)
