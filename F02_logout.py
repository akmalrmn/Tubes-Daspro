from F01_login import login
from time import sleep
from os import system

def logout(login_status, idx_usn, CSV_List):
  if login_status:
    sleep(0.5)
    print("Logout berhasil!")
    for j in range(idx_usn, 1000): # Melakukan penghapusan data yang dimasukkan saat melakukan login
      CSV_List[j] = CSV_List[j+1]
    CSV_List = [row for row in CSV_List if row] # list baru tanpa data yg dimasukkan user saat login
    login_status = False # logout berhasil
    sleep(1)
    system("cls")
  else: # belum melakukan login, login_status == False
    sleep(0.5)
    print("Logout gagal!")
    print("Anda belum login, silakan login terlebih dahulu sebelum melakukan logout!")
  return CSV_List, login_status