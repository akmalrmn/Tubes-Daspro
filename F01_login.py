from csvtolist import csv_to_list
from time import sleep
from os import system
from typing import List, Tuple, Union

def login(user_list: List[Union[str]], login_status: bool, idx_usn: int) -> Tuple[bool, int, List[str]]: # Fungsi login
    if login_status: # sudah login
        sleep(0.5)
        print("Login gagal!")
        print(f"Anda telah login dengan username {user_list[idx_usn][0]}, silahkan lakukan “logout” sebelum melakukan login kembali.")
    else: # belum login
        username = input("Username: ") # input username
        password = input("Password: ") # input password
        i = 1
        login_status = False
        while i <= 1000 and login_status == False : # Akan melakukan loop hingga login berhasil atau sudah membaca semua baris pada list user
            if username == user_list[i][0] :    #Cek apakah username valid
                if password == user_list[i][1] :    # Cek apakah password valid
                    sleep(0.5)
                    print()
                    system("cls")
                    if user_list[i][2] == "Pengumpul" or user_list[i][2] == "Pembangun":
                        print(f"🔥🔥🔥 Selamat datang, {username}! 🔥🔥🔥")
                        print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                    else:
                        print(f"Selamat datang, {username}!")
                        print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                    login_status = True # indikasi berhasil login
                    break # keluar dari while loop
                else :
                    sleep(0.5)
                    print("Password salah!")
                    break
            i += 1
        else: # gagal login
            sleep(0.5)
            print("Username tidak terdaftar!")
        return login_status, i, user_list
