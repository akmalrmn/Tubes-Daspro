file = open("user.csv", "r")
def jadi_array(nama_file, row, line):
    f = [[None for j in range(line)] for i in range(row)]
    i = 0
    j = 0
    value = ""
    with open(nama_file, 'r') as file:
        for line in file:
            for char in line:  # loop setiap karakter pada baris
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

login = False #Mengetahui status login

f = jadi_array('user.csv',3,3) #Memanggil function yang mengambil file 'user,csv' dan me assign dengan ukuran 3 baris dan 3 kolom atas nama f
bool = True
while bool : 
    print(">>> login")
    username = input("Username: ")  
    password = input("Password: ")
    if username == f[1][0] or username == f[2][0] : #Cek apakah username valid
        if password == f[1][1] or password == f[2][1] : # Cek apakah password valid
            print(f"Selamat datang, {username} !")
            login = True
            bool = False
        else :
            print("Password salah!")
    else :
        print("Username tidak terdaftar!")