import datetime

siswa = {
    "nama":"asepp",
    "jenis_kelamin":True,
    "nik":"4512",
    "sks":130,
    "lahir":datetime.datetime(2006,5,10)    
}
siswa1 = {
    "nama":"ucup",
    "jenis_kelamin":True,
    "nik":"451299977",
    "sks":120,
    "lahir":datetime.datetime(2006,9,12)    
}
siswa2 = {
    "nama":"pace",
    "jenis_kelamin":True,
    "nik":"4512114",
    "sks":190,
    "lahir":datetime.datetime(2006,10,8)    
}

# dictionary bersarang
data_collection = {
    "murid_1":siswa,
    "murid_2":siswa1,
    "murid_3":siswa2
    
}
print(f"\n{"key":<9} {'nama':<8} {'sks':<5} {'jenis kelamin':<15}{'lahir':^10}")
print("-"*49)

for murid in data_collection:
    key = murid
    nama = data_collection[key]['nama']
    sks = data_collection[key]['sks']
    jenis_kelamin = data_collection[key]['jenis_kelamin']
    lahir = data_collection[key]['lahir'].strftime("%x")
    
    print(f"\n{key:<9} {nama:<8} {sks:<5} {jenis_kelamin:^15} {lahir}")    