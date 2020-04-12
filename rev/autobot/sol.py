from pwn import *
import r2pipe
import sys

def solve(file):
    p = r2pipe.open(file)

    p.cmd('dor aslr=no,stdin=""')
    p.cmd('doo')
    p.cmd('aa')


    res = []
    bps = [
        0x5555555549b3,
    ]

    for i in bps:
        p.cmd('db '+hex(i))

    p.cmd('dbc 0x5555555549b3 dr rip=0x5555555549cd')

    # p.cmd('dc')
    # p.cmd('dr rip=0x555555555312')
    # p.cmd('dc')

    while True:
        reg = p.cmdj('drj')
        if not reg:
            print(reg)
            # binary exited
            break
        rax = reg['rax']
        if rax > 255:
            break
        res.append(rax)
        p.cmd('dc')
    password = (''.join(chr(i) for i in res))
    password = password[1:]
    return password

import tempfile
import base64
import time
import os, stat

def make_exec(file):
    os.chmod(file, stat.S_IXUSR | stat.S_IRUSR | stat.S_IWUSR)

# p = process('./server.py')
p = remote('13.234.59.79', 6000)
fil = tempfile.mktemp()
print(fil)
while True:
    t = p.recvline().strip()
    if b'flag' in t:
        print(t)
        break
    t = (base64.b64decode(t))
    # print(fil)
    try:
        os.remove(fil)
    except FileNotFoundError:
        print('asdf')
        pass
    open(fil, 'wb').write(t)
    make_exec(fil)
    log.info('solving')
    passw = (solve(fil))
    print(passw)
    p.sendline(passw)

p.interactive()
