# <--if stmt
x = int(input("masukkan angka: "))
if x < 0:
    print(f"negatif {x}")
elif x == 0:
    print(f"zerooo {x}")
elif x == 1:
    print(f"single {x}")
else:
    print(f"something {x}")
    
# <--for in stmt
# for in tuple
kata = ['kucing','sapi','anjing']
for alias in kata:
    print(alias,len(alias))

# for in collection
users = {
    "peltod":10,
    "ucup":90,
    "amir":80,
    "musa":999
}

# iterate menggunakan copy setiap items
for nama, no in users.copy().items():
    print(f"\nnama: {nama}\n\tid: {no}")

# *--studi kasus: user aktif
users={
    'hans':'active',
    'peltod':'active',
    'budi':'active',
    'asep':'inactive',
    'ucup':'active',
    'imron':'active',
}
# cek user yang off
inactive_users = {}        
for nama, status in users.copy().items():
    if status == 'inactive':
        inactive_users[nama] = status
        
# membuat collection user yang aktif
active_users = {}
for nama, status in users.copy().items():
    if status == 'active':
        active_users[nama] = status
    
for nama, status in users.copy().items():
    if status == 'inactive':
        del users[nama]

print(users)
print(active_users,end=" on\n")
print(inactive_users,end=" off\n\n")


# <-- range() function
for i in range(9):
    print(i)

a = ['asep','ucup','peltod','abyan']
for i in range(len(a)):
    print(f'\n',f'{i}:{a[i]}')

# ini menggunakan teknik looping

print(range(-219,100))

