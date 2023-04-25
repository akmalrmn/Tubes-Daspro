import os
import listtocsv

def save(user,candi,bahan_bangunan):
    def panjang_array(array):
            i = 0
            while True:
                if array[i][0] == None:
                    break
                else:
                    i += 1
            return i

    def array_bersih(array):
            arr = [None for i in range (panjang_array(array))]
            for i in range (panjang_array(array)):
                arr[i] = array[i]
            return arr

    def panjang_string(string):
        kata = string + "\n"
        jumlah = 0
        i = 0
        while kata[i] != "\n":
            jumlah += 1
            i += 1
        return jumlah

    print(">>> save\n")
    folder = input("Masukkan nama folder: ")
    folder = "save/" + folder
    print("\nSaving...\n")

    folder += "/"
    path = ''
    nama_folder = ''
    for i in range (panjang_string(folder)):
        if i < (panjang_string(folder)-1):
            nama_folder += folder[i]
        if folder[i] != "/":
            path += folder[i]
        else:
            if os.path.exists(path) == False:
                print(f"Membuat folder {path}...")
                os.mkdir(path)
                path += "/"
                
    if os.path.exists(path) == True:      
            listtocsv.list_to_csv(array_bersih(user),path,'user.csv')
            listtocsv.list_to_csv(array_bersih(candi),path,'candi.csv')
            listtocsv.list_to_csv(array_bersih(bahan_bangunan),path,'bahan_bangunan.csv')

    print(f"Berhasil Menyimpan data di folder {nama_folder}!")
