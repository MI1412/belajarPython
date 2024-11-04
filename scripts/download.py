import os
import requests

def download_pdfs_from_txt(file_path, download_folder):
    # Membuat folder download jika belum ada
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    
    # Membaca file txt untuk mendapatkan daftar tautan
    with open(file_path, 'r') as file:
        links = file.readlines()

    for index, link in enumerate(links):
        # Menghapus spasi atau newline dari setiap tautan
        link = link.strip()
        
        # Mengecek apakah link adalah PDF
        if link.endswith('.pdf'):
            try:
                # Mendapatkan nama file dari tautan
                file_name = os.path.basename(link)
                file_path = os.path.join(download_folder, file_name)
                
                # Mengunduh file PDF
                response = requests.get(link)
                response.raise_for_status()  # Mengecek apakah ada error dalam proses download
                
                # Menyimpan file PDF
                with open(file_path, 'wb') as pdf_file:
                    pdf_file.write(response.content)
                
                print(f'Successfully downloaded: {file_name}')
            except requests.exceptions.RequestException as e:
                print(f'Failed to download {link}: {e}')
        else:
            print(f'Skipped non-PDF link: {link}')

if __name__ == '__main__':
    # Ganti 'tautan.txt' dengan nama file .txt yang berisi tautan PDF
    txt_file_path = 'modified_output.txt'
    
    # Ganti 'pdf_downloads' dengan folder tujuan untuk menyimpan file PDF
    download_directory = 'pdf_downloads'
    
    # Memanggil fungsi untuk mengunduh file PDF
    download_pdfs_from_txt(txt_file_path, download_directory)
