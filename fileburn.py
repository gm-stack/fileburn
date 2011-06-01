#!/usr/bin/env python

import sys, random, stat, os

filename = sys.argv[1]
f = open(filename, 'rb+')
fsize = os.stat(filename)[stat.ST_SIZE]

print "Unlucky file is: %s" % filename

def corruptage(f,fsize):
    byte = random.randint(0,fsize)
    f.seek(byte)
    data = f.read(1)
    bdata = ord(data)
    corrBit = 2**random.randint(0,7)
    rbdata = bdata ^ corrBit
    print "0x%.8x %i -> %i" % (byte, bdata, rbdata)
    f.seek(byte)
    f.write(chr(rbdata))

for i in range(100):
    corruptage(f,fsize)