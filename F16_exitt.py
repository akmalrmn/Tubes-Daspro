from time import sleep
from animasi import animasiexit
from F14_save import save

def exitt(user, candi, bahan_bangunan):
  sleep(0.5)
  masukan = input("apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)").lower()
  while masukan != "y" and masukan != "n": # ketika input tidak sesuai
    sleep(0.5)
    masukan = input("apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)").lower()
  if masukan == "y":
    save(user, candi, bahan_bangunan)
  sleep(1)
  print("Exit berhasil")
  animasiexit()
  berhenti = True # indikasi tidak melakukan save dan akan keluar dari program
  return berhenti
