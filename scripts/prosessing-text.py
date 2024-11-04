def process_text_with_pattern(file_path, pattern, custom_text):
    # Membaca file .txt
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Menyimpan hasil modifikasi di list baru
    modified_lines = []

    for line in lines:
        # Mengecek apakah pola ada dalam baris
        if pattern in line:
            # Memisahkan teks sebelum dan setelah pola
            before_pattern, after_pattern = line.split(pattern, 1)

            # Menambahkan teks kustom sebelum pola dan merangkai ulang baris
            modified_line = f"{custom_text}{pattern}{after_pattern.strip()}"
            modified_lines.append(modified_line)
            print(f"Modified: {modified_line}")  # Menampilkan hasil perubahan
        else:
            # Jika pola tidak ditemukan, tetap menyimpan baris asli
            modified_lines.append(line.strip())

    # Menulis ulang hasil modifikasi ke file baru atau mengganti file asli
    with open('modified_output.txt', 'w') as output_file:
        output_file.write('\n'.join(modified_lines))

    print("\nTeks berhasil diproses dan disimpan di 'modified_output.txt'.")

if __name__ == '__main__':
    # Ganti 'teks.txt' dengan nama file .txt yang ingin diproses
    txt_file_path = 'tes.txt'
    
    # Ganti 'pola' dengan kata atau frasa yang ingin dicari
    search_pattern = 'rfc'
    
    # Ganti 'custom_text' dengan teks yang ingin Anda tambahkan sebelum pola
    custom_text_to_add = 'https://www.rfc-editor.org/pdfrfc/'

    # Memanggil fungsi untuk memproses teks
    process_text_with_pattern(txt_file_path, search_pattern, custom_text_to_add)
