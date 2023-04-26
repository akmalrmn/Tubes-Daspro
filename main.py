from commands import run
from time import sleep
import os
import argparse
from csvtolist import csv_to_list

# Mengubah semua file csv ke list in list
bahan_bangunan = csv_to_list("bahan_bangunan.csv", 5, 3)
candi = csv_to_list("candi.csv", 101, 5)
user = csv_to_list("user.csv", 1001, 3)

login_status = False  # status login
idx_usn = 1  # Indeks baris dari username saat melakukan login
idx_rng = 0  # Indeks list random number generator

# Set up argument parser
parser = argparse.ArgumentParser()
parser.add_argument("folder_name", nargs='?', help="Name of the folder to load files from")
args = parser.parse_args()

# Check if folder exists
folder_path = args.folder_name


if not folder_path:
    sleep(0.5)
    print("Tidak ada nama folder yang diberikan")
    print("\nUsage: python main.py <nama_folder>")
    exit()
folder_path = "save/" + folder_path
if not os.path.isdir(folder_path):
    sleep(0.5)
    print(f"Folder {folder_path} tidak ditemukan")
    exit()


sleep(0.5)
print('Loading...')
sleep(1)
print('Selamat datang di program “Manajerial Candi”')

# Load all files in folder
files = os.listdir(folder_path)
for file_name in files:
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        if file_name == "user.csv":
            user = csv_to_list(file_path, 1001, 3)
        elif file_name == "candi.csv":
            candi = csv_to_list(file_path, 101, 5)
        elif file_name == "bahan_bangunan.csv":
            bahan_bangunan = csv_to_list(file_path, 5, 3)

while True:
    sleep(0.8)
    masukan = input(">>> ")
    sleep(0.5)
    login_status, idx_usn, user, idx_rng, candi, bahan_bangunan = run(
        masukan, login_status, idx_usn, user, idx_rng, candi, bahan_bangunan)  # memanggil fungsi dari commands.py
    print()
