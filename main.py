from csvtolist import csv_to_list
from commands import run

bahan_bangunan = csv_to_list("bahan_bangunan.csv", 1001, 3)
candi = csv_to_list("candi.csv", 1001, 3)
user = csv_to_list("user.csv", 1001, 3)

login_status = False
i = None

while True:
  masukan = input(">>> ")
  login_status, i, user = run(masukan, login_status, i, user)
