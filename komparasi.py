#digunakan untuk membandingkan hasil
#operasi komparasi 
#setiap hasil perbandingan dari operasi komparasi adalah boolean
# > , <, >=, <=, ==, !=, is, is not 
#is membandingkan memori / objek / variabel jika sama true dan sebaliknya
#contoh : 
print("perbandingan is")
x = 5
z = 9
hasil = x is z
print("x adalah z = ",hasil)
#maka hasilnya false 

hasil = x is x
print("x adalah x = ",hasil)

print("perbandingan is not")
#isnot sebaliknya dari is
hasil = x is not z
print("x tidak sama z = ",hasil)
#hasilnya true 

hasil = x is not x 
print("x tidak sama x = ",hasil)