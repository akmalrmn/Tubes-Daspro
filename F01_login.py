from csvtolist import csv_to_list
from time import sleep
from os import system

def login(CSV_List, login_status, idx_usn): # Fungsi login
    if login_status: # sudah login
        sleep(0.5)
        print("Login gagal!")
        print(f"Anda telah login dengan username {CSV_List[idx_usn][0]}, silahkan lakukan “logout” sebelum melakukan login kembali.")
    else: # belum login
        username = input("Username: ") # input useername
        password = input("Password: ") # input password
        i = 1
        login_status = False
        while i <= 1000 and login_status == False : # Akan melakukan loop hingga login berhasil atau sudah membaca semua baris pada list user
            if username == CSV_List[i][0] :    #Cek apakah username valid
                if password == CSV_List[i][1] :    # Cek apakah password valid
                    sleep(0.5)
                    print()
                    system("cls")
                    if CSV_List[i][2] == "Pengumpul" or CSV_List[i][2] == "Pembangun":
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
        return login_status, i, CSV_List
