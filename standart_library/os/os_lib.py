# library os interface
import os

current_dir = os.getcwd()
print(f"direktori saat ini: {current_dir}")

os.chdir("e:")
echo = os.system("echo \"file os lib dijalankan\"")
crnt_dir = os.getcwd()
print(f"telah dipindah: {crnt_dir}")
print(f"menjalankan perintah echo: {echo}")



print(dir(os))

