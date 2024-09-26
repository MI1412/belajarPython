# **Ringkasan Dokumentasi tentang Menyimpan Data Terstruktur dengan JSON:**

# 1. **Penulisan dan Pembacaan Data:**
#    - Python memungkinkan untuk menulis dan membaca string ke/dari file dengan mudah. Namun, jika ingin menyimpan tipe data yang lebih kompleks seperti list bertingkat atau dictionary, proses parsing dan serialisasi secara manual akan menjadi rumit.
  
# 2. **JSON sebagai Format Pertukaran Data:**
#    - Python menyediakan modul standar bernama **json** untuk menangani data hierarki yang kompleks. Modul ini dapat mengonversi data Python menjadi representasi string (proses ini disebut **serialisasi**) dan dapat membangun kembali data dari string tersebut (**deserialisasi**).
#    - **JSON** (JavaScript Object Notation) merupakan format data populer yang sering digunakan untuk pertukaran data antar aplikasi. Banyak programmer yang sudah familiar dengan format ini, sehingga cocok untuk **interoperabilitas**.

# 3. **Contoh Serialisasi:**
#    - Untuk melihat representasi JSON dari objek Python, misalnya list:
#      
import json
x = [1, 'simple', 'list']
print(json.dumps(x))  # Menghasilkan: '[1, "simple", "list"]'
     

# 4. **Penulisan ke File:**
#    - Anda dapat menyimpan objek yang diserialisasikan ke file teks menggunakan **`json.dump()`**.
#
with open('file.json', 'w', encoding='utf-8') as f:
    json.dump(x, f)
#      

# 5. **Membaca dari File:**
#    - Untuk memuat objek yang telah diserialisasikan dari file teks atau file biner, gunakan **`json.load()`**.
#      
with open('file.json', 'r', encoding='utf-8') as f:
    x = json.load(f)
    print('memuat: {0}'.format(x))
     

# 6. **Catatan Penting:**
#    - File JSON harus dienkode dalam format **UTF-8**. Saat membuka file JSON untuk membaca atau menulis, pastikan menggunakan **`encoding="utf-8"`**.

# 7. **Serialisasi Objek Kelas:**
#    - Meskipun JSON dapat menangani list dan dictionary, serialisasi instance dari kelas khusus membutuhkan usaha tambahan. Dokumentasi modul **json** memiliki penjelasan lebih lanjut tentang ini.

# 8. **Modul Lain: pickle**
#    - Modul **pickle** di Python memungkinkan serialisasi objek Python yang lebih kompleks. Namun, berbeda dengan JSON, **pickle** tidak bisa digunakan untuk berkomunikasi dengan aplikasi dari bahasa lain.
#    - **Peringatan:** Deserialisasi data **pickle** dari sumber yang tidak dipercaya bisa berbahaya, karena dapat mengeksekusi kode arbitrer jika datanya telah dimanipulasi oleh penyerang yang terampil.

# **Kesimpulan:**  
# JSON adalah format pertukaran data yang umum digunakan dan mudah dipahami, cocok untuk komunikasi antar aplikasi. Modul **json** di Python memberikan cara yang efisien untuk menyimpan dan memuat data terstruktur seperti list dan dictionary, tetapi membutuhkan penanganan khusus untuk objek yang lebih kompleks.