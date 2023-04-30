from typing import List

def panjang(x: List[str]) -> int: # menghitung panjang array
        j = 0
        while True:
            if x[j][0] == None:
                break
            else:
                j += 1
        return j

def count_kata_jin(user_list: List[str]) -> int: # menghitung banyak jin
    jumlah_baris = panjang(user_list)
    jumlah = 0
    for i in range (panjang(user_list)):
        if user_list[i][2] == "Pembangun" or user_list[i][2] == "Pengumpul":
            jumlah += 1
    return jumlah

def cekusername(usn:str, arr: List[str]) -> bool: # mengecek username apakah sudah ada pada list
    valid = False
    for i in range(panjang(arr)):
        if arr[i][0] == usn:
            valid = True
    return valid

from time import sleep
from animasi import animasijin

def summonjin(user_list: List[str], i: int) -> List[str] | None:
    if count_kata_jin(user_list) >= 100:
        print('Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu')
        return None
    elif user_list[i][0] == "Bondowoso":
        print('''Jenis jin yang dapat dipanggil:
        (1) Pengumpul - Bertugas mengumpulkan bahan bangunan
        (2) Pembangun - Bertugas membangun candi
        ''')
        bool_nomor_jin = True
        while bool_nomor_jin:
            sleep(0.5)
            nomor_jin = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
            sleep(0.5)
            if nomor_jin != "1" and nomor_jin != "2":
                sleep(0.5)
                print(f"Tidak ada jenis jin bernomor “{nomor_jin}”!")
                print()
            elif nomor_jin == '1':
                print()
                bool_nomor_jin = False
                print('Memilih jin “Pengumpul”.')
                bool_username_jin = True
                while bool_username_jin:
                    sleep(0.5)
                    username_jin = input('Masukkan username jin: ')
                    if cekusername(username_jin, user_list): #buat cara mengetahui apakah username_jin sudah ada di matriks
                        sleep(0.5)
                        print(f'Username {username_jin} sudah diambil!')
                        print()
                    else: #jika username_jin belum ada maka buat password
                        # buat loop sampai password memiliki len 5-25
                        bool_username_jin = False
                        bool_password = True
                        while bool_password:
                            password_jin = input('Masukkan password jin: ')
                            print()
                            if len(password_jin) > 4 and len(password_jin) < 26:
                                sleep(0.5)
                                print(f'''Mengumpulkan sesajen...
                                Menyerahkan sesajen...
                                Membacakan mantra...
                                Jin {username_jin} berhasil dipanggil!''')
                                new_data = [username_jin,password_jin,'Pengumpul']
                                # Mengganti baris pada indeks yang ditemukan dengan data baru
                                panjangg = panjang(user_list)
                                for i in range(3):
                                    user_list[panjangg][i] = new_data[i]
                                print()
                                animasijin()
                                bool_password = False
                            else: #jika panjang password tidak 5 sampai 25 karakter
                                sleep(0.5)
                                print('Password panjangnya harus 5-25 karakter!')
            else: # untuk nomor jin == 2
                bool_nomor_jin = False
                print()
                print('Memilih jin “Pembangun”.')
                bool_username_jin = True
                while bool_username_jin:
                    username_jin = input('Masukkan username jin: ')
                    if cekusername(username_jin, user_list): #buat cara mengetahui apakah username_jin sudah ada di matriks
                        sleep(0.5)
                        print(f'Username {username_jin} sudah diambil!')
                        print()
                    else: #jika username_jin belum ada maka buat password
                        # buat loop sampai password memiliki len 5-25
                        bool_username_jin = False
                        bool_password = True
                        while bool_password:
                            password_jin = input('Masukkan password jin: ')
                            print()
                            if len(password_jin) > 4 and len(password_jin) < 26:
                                sleep(0.5)
                                print(f'''Mengumpulkan sesajen...
                                Menyerahkan sesajen...
                                Membacakan mantra...
                                Jin {username_jin} berhasil dipanggil!''')
                                new_data = [username_jin,password_jin,'Pembangun']
                                # Mengganti baris pada indeks yang ditemukan dengan data baru
                                panjangg = panjang(user_list)
                                for i in range(3):
                                    user_list[panjangg][i] = new_data[i]
                                print()
                                animasijin()
                                bool_password = False
                            else: #jika panjang password tidak 5 sampai 25 karakter
                                sleep(0.5)
                                print('Password panjangnya harus 5-25 karakter!')
    else:
        print("Program ini hanya dapat diakses oleh Bondowoso")
    return user_list