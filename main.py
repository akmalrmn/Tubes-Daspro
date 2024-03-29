from commands import run
from time import sleep
import os
import argparse
from csvtolist import csv_to_list
from F13_load import load

# Mengubah semua file csv ke list in list
user, candi, bahan_bangunan = load()

login_status = False  # status login
idx_usn = 1  # Indeks baris dari username saat melakukan login
idx_rng = 0  # Indeks list random number generator 1 - 5
idx_rng2 = 0 # Indeks list random number generator 0 - 5

while True:
    sleep(0.8)
    masukan = input(">>> ")
    sleep(0.5)
    login_status, idx_usn, user, idx_rng, candi, idx_rng2, bahan_bangunan = run(
        masukan, login_status, idx_usn, user, idx_rng, candi, idx_rng2, bahan_bangunan)  # memanggil fungsi dari commands.py
    print()
