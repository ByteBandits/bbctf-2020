p = 0
hsh1 = 0
hsh2 = 0
mod = int(1e9 + 7)
mod2 = int(1e9 + 9)
f = open("hashes.txt").read().split("\n")
for i in range(10000):
    f[i] = f[i].split()
    f[i] = (int(f[i][0]), int(f[i][1]))
d = {}
for i in f:
    d[i] = 0

l1 = []
l2 = []

a = 1
b = 1
for i in range(1001):
    l1.append(a)
    l2.append(b)
    a = (a * 31) % mod
    b = (b * 31) % mod2

c = 0
for i in range(20):
    s = open("a/" + str(i)).read()
    la = []
    la.append(0)
    lb = []
    lb.append(0)
    h1 = 0
    h2 = 0

    for i in range(len(s)):
        h1 += ((ord(s[i]) - 96) * pow(31, i, mod)) % mod
        h2 += ((ord(s[i]) - 96) * pow(31, i, mod2)) % mod2
        la.append(h1)
        lb.append(h2)

    for i in range(len(s)):
        for j in range(i, min(i + 101, len(s))):
            h1 = ((la[j + 1] - la[i]) * pow(l1[i], mod - 2, mod)) % mod
            h2 = ((lb[j + 1] - lb[i]) * pow(l2[i], mod2 - 2, mod2)) % mod2
            if d.get((h1, h2)) is not None:
                if d[(h1, h2)] == 0:
                    c += 1
                d[(h1, h2)] = j - i + 1
    print(c)

c2 = 0
a = 0
for i in range(10000):
    a += 1
    hsh1 += (pow(31, p, mod) * f[i][0]) % mod
    hsh1 %= mod
    hsh2 += (pow(31, p, mod2) * f[i][1]) % mod2
    hsh2 %= mod2
    p += d[f[i]]

print(hsh1, hsh2)
