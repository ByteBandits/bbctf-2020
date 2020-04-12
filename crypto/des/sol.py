def power(x, y, p) : 
    res = 1
    x = x % p
    while (y > 0):  
        if (y & 1): 
            res = (res * x) % p  
        y = y >> 1
        x = (x * x) % p  
    return res  
def squareRoot(n, p):  
    n = n % p  
    x = power(n, (p + 1) // 4, p)  
    if ((x * x) % p == n):  
        return x
    x = p - x  
    if ((x * x) % p == n):
        return x
    print("ERROR")

import ast, base64
from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.Cipher import DES

s = open('result.txt', 'r').read().split('\n')
# result.txt contains the output of get key and encrypted flag separated by newline character

l = ast.literal_eval(s[1])

m = int(s[0], 16)

for i in range(len(l)):
    l[i] = int(l[i], 16)

c = base64.b64decode(s[2])

l2 = []


key = b''

for i in range(128):
    x=65536
    while(x!=1):
        l[i]=squareRoot(l[i], m)
        x=x/2
    l[i]=l[i]%m
    l[i]=min(l[i], m-l[i])
    l[i]=long_to_bytes(l[i])
    key+=l[i][:8]
    l2.append(bytes_to_long(l[i][8:]))

l2.reverse()

for i in range(128):
    cipher = DES.new(key[l2[i]:l2[i]+8], DES.MODE_ECB)
    c = cipher.decrypt(c)

print(c)
