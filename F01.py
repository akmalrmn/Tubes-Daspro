def jadi_array(nama_file, row, collumns):
    f = [[None for j in range(collumns)] for i in range(row)]
    i = 0
    j = 0
    value = ""
    with open(nama_file, 'r') as file:
        for collumns in file:
            for char in collumns:  # loop setiap karakter pada baris
                if char == ";" or char =='\n':  # jika ditemukan titik koma, maka simpan nilai dalam array f
                    f[i][j] = value
                    value = ""
                    j += 1
                    if j >= 3:  # reset kolom jika sudah mencapai batas kolom maksimal
                        j = 0
                        i += 1
                else:  # tambahkan karakter ke nilai yang sedang dibaca
                    value += char
    return f

def login():
    f = jadi_array("user.csv",101,3) #Memanggil function yang mengambil file 'user,csv' dan me assign dengan ukuran 101 baris dan 3 kolom atas nama f
    username = input("Username: ")  
    password = input("Password: ")
    i = 1
    login_status = False
    while i <= 101 and login_status == False :
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
