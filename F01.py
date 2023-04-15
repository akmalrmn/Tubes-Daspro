def jadi_array(nama_file, row, collumns): # Fungsi parsing CSV statis
    CSV_List = [[None for j in range(collumns)] for i in range(row)] # CSV yang sudah diparsing akan dimasukkan ke variabel CSV_List
    i = 0
    j = 0
    value = ""
    with open(nama_file, 'r') as file:
        for collumns in file:
            for char in collumns:  # loop setiap karakter pada baris
                if char == ";" or char == '\n':  # jika ditemukan titik koma, maka simpan nilai dalam array f
                    CSV_List[i][j] = value
                    value = ""
                    j += 1
                    if j >= 3:  # reset kolom jika sudah mencapai batas kolom maksimal
                        j = 0
                        i += 1
                else:  # tambahkan karakter ke nilai yang sedang dibaca
                    value += char
    return CSV_List

def login(): # Fungsi login
    f = jadi_array("user.csv", 1001, 3) #Memanggil function yang mengambil file 'user.csv' dan melakukan assign dengan ukuran 1001 baris dan 3 kolom atas nama f
    username = input("Username: ")  
    password = input("Password: ")
    i = 1
    login_status = False
    while i <= 1001 and login_status == False :
        if username == f[i][0] :    #Cek apakah username valid
            if password == f[i][1] :    # Cek apakah password valid
                print(f"Selamat datang, {username}!")
                print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                login_status = True
            else :
                print("Password salah!")
                login_status = True
        else :
            print("Username tidak terdaftar!")
            break
