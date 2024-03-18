# widht and multiline
# data 
data_nama = "muhammad imron"
data_umur = 17
data_tinggi = 160

# string standart
data_string = f"nama {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}\n"
print(5*"=","data string biasa",5*"=")
print(data_string)

# string multiline dengan menggunakan new line dan tab
data_string = f"nama \t= {data_nama}\numur \t= {data_umur}\ntinggi \t= {data_tinggi}\n"
print(5*"=","data string multiline",5*"=")
print(data_string)

# string multiline dengan menggunakan kutip dua sampai tiga kali dan tab
data_string = f"""
nama \t\t= {data_nama:>5} 
umur sebelum\t= {data_umur}
umur sesudah\t= {data_umur:>5}
tinggi sebelum\t= {data_tinggi}
tinggi sesudah\t= {data_tinggi:>5}
""" # digunakan untuk mengatur lebar
print(5*"=","data string multiline dengan kutip \" sampai 3x",5*"=")
print(data_string)