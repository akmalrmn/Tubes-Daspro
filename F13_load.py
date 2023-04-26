import os
import argparse
from time import sleep
from csvtolist import csv_to_list

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
sleep(0.3)
print('Silahkan masukkan username Anda')
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
