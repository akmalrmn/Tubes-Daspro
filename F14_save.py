import os
import listtocsv
from time import sleep
from typing import List, Union

def save(user: List[str], candi: List[Union[str, int]], bahan_bangunan: List[Union[str, int]]) -> None:
    def panjang_string(string): # menghitung panjang string
        kata = string + "\n"
        jumlah = 0
        i = 0
        while kata[i] != "\n":
            jumlah += 1
            i += 1
        return jumlah
    # input nama folder
    folder = input("Masukkan nama folder: ")
    folder = "save/" + folder
    sleep(1)
    print("\nSaving...\n")

    folder += "/"
    path = ''
    nama_folder = ''
    for i in range (panjang_string(folder)):
        if i < (panjang_string(folder)-1):
            nama_folder += folder[i]
        if folder[i] != "/": # menuliskan path
            path += folder[i]
        else:
            if os.path.exists(path) == False: # belum ada folder yg dituju
                sleep(0.5)
                print(f"Membuat folder {path}...")
                os.mkdir(path)
                path += "/"
            else:
                path += "/"
                
    if os.path.exists(path) == True: # ada  folder yg dituju      
            listtocsv.list_to_csv(user,path,'user.csv') # mengubah list yang disimpan ke csv
            listtocsv.list_to_csv(candi,path,'candi.csv')
            listtocsv.list_to_csv(bahan_bangunan,path,'bahan_bangunan.csv')
    print()
    sleep(1)
    print(f"Berhasil Menyimpan data di folder {nama_folder}!")