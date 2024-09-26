# <--break, continue, else clause
# contoh penggunaan break
# logika menentukan angka equal dan angka prime
for i in range(2, 10):
    for x in range(2, i):
        if i % x == 0:
            print(i, 'mirip:', x, '*', i // x)
            break
    else:
        # Blok ini dieksekusi jika tidak ditemukan pembagi
        print(i, 'angka prima')


