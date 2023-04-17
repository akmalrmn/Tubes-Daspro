from csvtolist import csv_to_list
from commands import run

bahan_bangunan = csv_to_list("bahan_bangunan.csv", 4, 3)
candi = csv_to_list("candi.csv", 1001, 5)
user = csv_to_list("user.csv", 1001, 3)

login_status = False
idx_usn = 1
idx_rng = 1

for i in range(1, 4):
  bahan_bangunan[i][2] = 0

while True:
  masukan = input(">>> ")
  if masukan == "kumpul":
    login_status, idx_usn, bahan_bangunan, idx_rng = run(masukan, login_status, idx_usn, bahan_bangunan, idx_rng)
    idx_rng += 1
  else:
    login_status, idx_usn, user,idx_rng = run(masukan, login_status, idx_usn, user, idx_rng)