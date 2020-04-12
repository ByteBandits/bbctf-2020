from pwn import *
import sys
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

print(solve(sys.argv[1]))
