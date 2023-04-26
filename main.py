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

while True:
    sleep(0.8)
    masukan = input(">>> ")
    sleep(0.5)
    login_status, idx_usn, user, idx_rng, candi, bahan_bangunan = run(
        masukan, login_status, idx_usn, user, idx_rng, candi, bahan_bangunan)  # memanggil fungsi dari commands.py
    print()
