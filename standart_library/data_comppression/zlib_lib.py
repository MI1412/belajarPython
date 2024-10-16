import zlib
# NAME
#     zlib

data = b"lorem lorema lmdlam admlma pmpad mdapdmpa"
panjang = len(data)
print(panjang)
data_compress = zlib.compress(data)
panjang = len(data_compress)
print(panjang)

decompress = zlib.decompress(data_compress)
print(decompress)

crc32 = zlib.crc32(data)
print(crc32)
