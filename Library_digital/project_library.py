# project membuat perpustakaan digital
import os   
import CRUD as CRUD
if __name__ == '__main__':
        syst_operasi = os.name
        match syst_operasi: # match adalah semacam syntax switch di python
            case 'posix': os.system('clear')
            case 'nt': os.system('cls')
        print('selamat datang di perpustakaan digital :)')
        print(50*'=')
        
        # cek database
        CRUD.init_console()
        
        while(True):    
            print(f'1. Read Data \n2. Create Data \n3. Update Data \n4. Delete Data \n')
            user_option = int(input('masukkan opsi : '))
            
            match user_option:
                case 1: CRUD.read_console()
                case 2: 
                    CRUD.create_console()
                case 3: 
                    print('ini Update Data')
                case 4: 
                    print('ini Delete Data')
                case _:
                    print('tidak ada opsi yang dipilih')
            is_done = input('\nApakah selesai (Y/N)? : ')
            if is_done == 'y' or is_done == 'Y':
                break
            
        
print('thanks')