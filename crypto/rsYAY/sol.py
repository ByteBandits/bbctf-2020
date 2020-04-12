import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
while(True):
	u = base64.b64decode(input('plaintext : ').encode())
	x = int(input('X : '), 16)
	m = int(input('M : '), 16)

	n = ((x-1)*pow(4, m-2, m))%m

	a = RSA.construct((n, 65537))

	encryptor = PKCS1_OAEP.new(a)
	print("Answer : ")
	print(base64.b64encode(encryptor.encrypt(u)).decode())
