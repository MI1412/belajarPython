# NAME
    # argparse - Command-line parsing library

import argparse
import sys

uraikan = argparse.ArgumentParser(prog="header",description="deskripsi dari beberapa file ini")
uraikan.add_argument("filenames",nargs="+")
uraikan.add_argument("-l","--lines", type=int, default=10)
args = uraikan.parse_args()

# pemindahan error output
# sys.stderr.write("!!, log: file ga nemu oi")
print(args)