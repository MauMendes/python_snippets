# code snippets 

import zlib, sys

filename_in = "data"
filename_out = "compressed_data"

with open(filename_in, mode="rb") as fin, open(filename_out, mode="wb") as fout:
    data = fin.read()
    compressed_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
    print(f"Original size: {sys.getsizeof(data)}")
    # Original size: 1000033
    print(f"Compressed size: {sys.getsizeof(compressed_data)}")
    # Compressed size: 1024

    fout.write(compressed_data)

with open(filename_out, mode="rb") as fin:
    data = fin.read()
    compressed_data = zlib.decompress(data)
    print(f"Compressed size: {sys.getsizeof(data)}")
    # Compressed size: 1024
    print(f"Decompressed size: {sys.getsizeof(compressed_data)}")
    # Decompressed size: 1000033

#### EXAMPLE 2
import bz2, os, sys

filename_in = "data"
filename_out = "compressed_data.bz2"

with open(filename_in, mode="rb") as fin, bz2.open(filename_out, "wb") as fout:
    fout.write(fin.read())

print(f"Uncompressed size: {os.stat(filename_in).st_size}")


#### EXAMPLE 3
import lzma, os
lzc = lzma.LZMACompressor()

# cat /usr/share/dict/words | sort -R | head -c 1MB > data
filename_in = "data"
filename_out = "compressed_data.xz"

with open(filename_in, mode="r") as fin, open(filename_out, "wb") as fout:
    for chunk in fin.read(1024):
        compressed_chunk = lzc.compress(chunk.encode("ascii"))
        fout.write(compressed_chunk)
    fout.write(lzc.flush())

print(f"Uncompressed size: {os.stat(filename_in).st_size}")
# Uncompressed size: 972398
print(f"Compressed size: {os.stat(filename_out).st_size}")
# Compressed size: 736

with lzma.open(filename_out, "r") as fin:
    words = fin.read().decode("utf-8").split()
    print(words[:5])
    # ['dabbing', 'hauled', "seediness's", 'Iroquoian', 'vibe']
# Uncompressed size: 1000000
print(f"Compressed size: {os.stat(filename_out).st_size}")
# Compressed size: 48

with bz2.open(filename_out, "rb") as fin:
    data = fin.read()
    print(f"Decompressed size: {sys.getsizeof(data)}")
    # Decompressed size: 1000033
    
### EXAMPLE 4
import os, sys, shutil, gzip

filename_in = "data"
filename_out = "compressed_data.tar.gz"

with open(filename_in, "rb") as fin, gzip.open(filename_out, "wb") as fout:
    # Reads the file by chunks to avoid exhausting memory
    shutil.copyfileobj(fin, fout)

print(f"Uncompressed size: {os.stat(filename_in).st_size}")
# Uncompressed size: 1000000
print(f"Compressed size: {os.stat(filename_out).st_size}")
# Compressed size: 1023

with gzip.open(filename_out, "rb") as fin:
    data = fin.read()
    print(f"Decompressed size: {sys.getsizeof(data)}")
    # Decompressed size: 1000033
