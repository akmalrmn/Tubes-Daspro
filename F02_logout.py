from F01_login import login
from time import sleep
from os import system
from typing import List, Tuple

def logout(login_status: bool, idx_usn: int, user_list: List[str]) -> Tuple[List[str], bool]:
  if login_status:
    sleep(0.5)
    print("Logout berhasil!")
    for j in range(idx_usn, 1000): # Melakukan penghapusan data yang dimasukkan saat melakukan login
      user_list[j] = user_list[j+1]
    user_list[1000] = [None, None, None] # list baru tanpa data yg dimasukkan user saat login
    login_status = False # logout berhasil
    sleep(1)
    system("cls")
    print("tekan (help) untuk melihat opsi yang tersedia")
  else: # belum melakukan login, login_status == False
    sleep(0.5)
    print("Logout gagal!")
    print("Anda belum login, silakan login terlebih dahulu sebelum melakukan logout!")
  return user_list, login_status