from csvtolist import csv_to_list

def login(): # Fungsi login
    CSV_List = csv_to_list("user.csv", 1001, 3) #Memanggil function yang mengambil file 'user.csv' dan melakukan assign dengan ukuran 1001 baris dan 3 kolom atas nama CSV_list
    username = input("Username: ")  
    password = input("Password: ")
    i = 1
    login_status = False
    while i <= 1001 and login_status == False :
        if username == CSV_List[i][0] :    #Cek apakah username valid
            if password == CSV_List[i][1] :    # Cek apakah password valid
                print(f"Selamat datang, {username}!")
                print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                login_status = True
                return login_status
            else :
                print("Password salah!")
                break
        else :
            print("Username tidak terdaftar!")
            break
