from time import sleep
from typing import Union, List, Tuple

def hancurkan_candi(arr_candi: List[Union[str, int]], idx_usn: int, user: List[str]) -> List[Union[str, int]]:  
    if user[idx_usn][0] == "Roro":
        # Input id candi 
        id_candi = int(input('Masukan ID candi: '))

        # Cek apakah ada candi dengan ID tersebut dan declare atas nama valid
        valid = False
        i = 0
        while i < 102:
            if arr_candi[i][0] == id_candi:
                valid = True
                break
            else:
                i += 1
        # Algoritma Hancurkan_candi
        if not valid :
            sleep(0.5)
            print('Tidak ada candi dengan ID tersebut.')        
        else :
            pilihan = input(f'Apakah anda yakin ingin menghancurkan candi ID: {id_candi} (Y/N)? ')
            if pilihan == 'Y' :
                # cari baris candi dengan ID tersebut
                loop = True
                row_num = 0
                i = 0
                while loop:
                    if arr_candi[i][0] != id_candi:
                        i += 1
                        row_num += 1
                    else :
                        loop = False
                for j in range(row_num, 101): # Melakukan penghapusan data yang dimasukkan saat melakukan login
                    arr_candi[j] = arr_candi[j+1]
                    arr_candi[101] = [None, None, None, None, None] # list baru tanpa data yg dimasukkan user saat login
                sleep(0.5)
                print()
                print("Candi berhasil dihancurkan")
            else:
                sleep(0.5)
                print()
                print("Candi gagal dihancurkan.")
    else:
        sleep(0.5)
        print("Program ini hanya dapat diakses oleh Roro")
    return arr_candi