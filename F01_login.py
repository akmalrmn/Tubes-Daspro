from csvtolist import csv_to_list

def login(CSV_List): # Fungsi login
    username = input("Username: ")  
    password = input("Password: ")
    i = 1
    login_status = False
    while i <= 1000 and login_status == False :
        if username == CSV_List[i][0] :    #Cek apakah username valid
            if password == CSV_List[i][1] :    # Cek apakah password valid
                print(f"Selamat datang, {username}!")
                print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                login_status = True
                break
            else :
                print("Password salah!")
                return login_status, i, CSV_List
                break
        i += 1
    if login_status == False:
        print("Username tidak terdaftar!")
        return login_status, i, CSV_List
    return login_status, i, CSV_List
