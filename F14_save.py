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

    def panjang_string(string):
        kata = string + "\n"
        jumlah = 0
        i = 0
        while kata[i] != "\n":
            jumlah += 1
            i += 1
        return jumlah
    
    def array_bersih(array):
        arr = [None for i in range (panjang_array(array))]
        for i in range (panjang_array(array)):
            arr[i] = array[i]
        return arr

    
    folder = input("Masukkan nama folder: ")
    folder = f"save/{folder}"
    print("\nSaving...\n")
    folder += "/"
    jumlah = 0
    for i in range(panjang_string(folder)):
        if folder[i] == "/":
            jumlah += 1
    i = 0
    batas = 0
    path = ""
    while batas != jumlah:
        if folder[i] != "/":
            path += folder[i]
            i += 1
        else:
            if os.path.exists(path) == False:
                print(f"Membuat folder {path}...")
                os.mkdir(path)
            batas += 1
            path += folder[i]
            i += 1
    if os.path.exists(path) == True:      
        listtocsv.list_to_csv(array_bersih(user),path,'user.csv')
        listtocsv.list_to_csv(array_bersih(candi),path,'candi.csv')
        listtocsv.list_to_csv(array_bersih(bahan_bangunan),path,'bahan_bangunan.csv')