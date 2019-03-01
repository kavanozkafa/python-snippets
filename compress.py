import zlib
string = "sammas colkesen"
t = zlib.compress(string.encode("utf-8"))
print(t) # b'x\x9c+N\xcc\xcdM,VH\xce\xcf\xc9N-N\xcd\x03\x00/m\x05\xf7'
print(zlib.decompress(t)) # b'sammas colkesen'
