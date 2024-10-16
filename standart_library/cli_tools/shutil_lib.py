# NAME
    # shutil - Utility functions for copying and archiving files and directory trees.

import shutil

file_cp = shutil.copy("os_lib.py","filecp.txt")

print(file_cp)

file_mv = shutil.move("tes/","dimove")
print(file_mv)