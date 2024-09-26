# Ketika paket terstruktur ke dalam subpaket (seperti pada contoh paket sound), Anda dapat menggunakan impor absolut untuk merujuk ke submodul dari paket saudara. Misalnya, jika modul sound.filters.vocoder perlu menggunakan modul echo dari paket sound.effects, Anda dapat menggunakan from sound.effects import echo.

# Anda juga dapat menulis impor relatif, dengan bentuk pernyataan impor from module import name. Impor ini menggunakan titik-titik di depan untuk menunjukkan paket saat ini dan paket induk yang terlibat dalam impor relatif. Dari modul surround, misalnya, Anda bisa menggunakan:
# from . import echo
# from .. import formats
# from ..filters import equalizer

# Perhatikan bahwa impor relatif didasarkan pada nama modul saat ini. Karena nama modul utama selalu "main", modul yang dimaksudkan untuk digunakan sebagai modul utama dari aplikasi Python harus selalu menggunakan impor absolut.

# Kesimpulan:

# Impor Absolut: Digunakan untuk merujuk submodul dari paket lain, contohnya from sound.effects import echo untuk mengakses modul echo dari paket sound.effects ketika berada di modul sound.filters.vocoder.

# Impor Relatif: Menggunakan titik-titik untuk menunjukkan paket saat ini dan paket induk. Misalnya, from . import echo mengimpor modul echo dari paket yang sama, dan from ..filters import equalizer mengimpor submodul equalizer dari paket induk.

# Modul Utama: Modul yang digunakan sebagai modul utama dari aplikasi Python harus menggunakan impor absolut karena nama modul utama adalah "main" dan tidak cocok untuk impor relatif.