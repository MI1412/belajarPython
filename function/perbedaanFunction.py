# function dengan kurung akan memanggil fungsinya sendiri
def halo():
	return "halo"
print(f"function default{halo()}")

# function tanpa kurung hanya dipanggil referensi saja
def hai():
	return "hai"
#referensi funct
hai_funct = hai
print(f"reff funct: {hai_funct()}")

# Penggunaan ini sangat penting dalam konteks seperti callback, event #handling, atau ketika Anda ingin menyimpan referensi fungsi untuk #digunakan nanti.