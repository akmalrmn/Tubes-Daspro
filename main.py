from csvtolist import csv_to_list
from commands import run

# Mengubah semua file csv ke list in list
bahan_bangunan = csv_to_list("bahan_bangunan.csv", 4, 3) 
candi = csv_to_list("candi.csv", 1001, 5)
user = csv_to_list("user.csv", 1001, 3)

login_status = False # status login
idx_usn = 1 # Indeks baris dari username saat melakukan login
idx_rng = 0 # Indeks list random number generator
csvlist2 = []

for i in range(1, 4):
  bahan_bangunan[i][2] = 0 # Melalkukan pengisian list bahan bangunan agar dapat di-assign

while True:
  masukan = input(">>> ")
  if masukan == "kumpul":
    login_status, idx_usn, bahan_bangunan, idx_rng, csvlist2 = run(masukan, login_status, idx_usn, bahan_bangunan, idx_rng, csvlist2)
    idx_rng += 1 # index rng bertambah agar saat dipanggil kembali, akan mengeluarkan number yg berbeda
  elif masukan == "hapusjin":
    login_status, idx_usn, user, idx_rng, candi = run(masukan, login_status, idx_usn, user, idx_rng, candi)
  else:
    login_status, idx_usn, user, idx_rng, csvlist2 = run(masukan, login_status, idx_usn, user, idx_rng, csvlist2)
    