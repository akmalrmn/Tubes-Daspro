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
    status = False
    f = jadi_array('user.csv',3,101) #Memanggil function yang mengambil file 'user,csv' dan me assign dengan ukuran 3 baris dan 3 kolom atas nama f
    username = input("Username: ")  
    password = input("Password: ")
    if username == f[1][0] or username == f[2][0] : #Cek apakah username valid
        if password == f[1][1] or password == f[2][1] : # Cek apakah password valid
            print(f"Selamat datang, {username} !")
        else :
            print("Password salah!")
    else :
        print("Username tidak terdaftar!")
    
    return
