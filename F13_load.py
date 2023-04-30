import os
import argparse
from time import sleep
from csvtolist import csv_to_list
from typing import Tuple, Union, List

def load() -> Tuple[List[str], List[Union[str, int]], List[Union[str, int]]]:
    # fungsi parser
    parser = argparse.ArgumentParser()
    parser.add_argument("folder_name", nargs='?', help="Name of the folder to load files from")
    args = parser.parse_args()

    folder_path = args.folder_name
    
    if not folder_path: # apabila tidak menginput nama folder
        sleep(0.5)
        print("Tidak ada nama folder yang diberikan")
        print("\nUsage: python main.py <nama_folder>")
        exit()
    if not os.path.isdir("save/" + folder_path): # tidak ada nama folder
        sleep(0.5)
        print(f"Folder {folder_path} tidak ditemukan")
        exit()
    folder_path = "save/" + folder_path
    sleep(0.5)
    print('Loading...')
    sleep(1)
    print('Selamat datang di program “Manajerial Candi”')
    print()
    sleep(0.7)
    print('Silahkan "login" terlebih dahulu, atau "help" untuk melihat opsi yang tersedia.')
    sleep(0.3)
    print("Buka terminal sebesar mungkin untuk pengalaman yang maksimal")
    files = os.listdir(folder_path)
    for file_name in files: # for line in f (diperbolehkan)
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path): 
            if file_name == "user.csv": # mengubah csv ke list untuk setiap file name
                user = csv_to_list(file_path, 1001, 4)
            elif file_name == "candi.csv":
                candi = csv_to_list(file_path, 102, 6)
            elif file_name == "bahan_bangunan.csv":
                bahan_bangunan = csv_to_list(file_path, 6, 4)
    if bahan_bangunan[1][0] == None: # apabila bahan bangunan masih kosong, sehingga diassign agar lebih gampang diakses pada program lainnya
        bahan = ["pasir", "batu", "air"]
        for i in range(1,4):
            bahan_bangunan[i][0] = bahan[i-1]
            bahan_bangunan[i][1] = f"{bahan[i-1]} yang tersedia"
            bahan_bangunan[i][2] = 0
    return user, candi, bahan_bangunan