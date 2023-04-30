from time import sleep
from animasi import animasiexit
from F14_save import save
from typing import List, Union

def exitt(user: List[str], candi: List[Union[str, int]], bahan_bangunan: List[Union[str, int]]) -> None:
  sleep(0.5)
  masukan = input("apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)").lower()
  while masukan != "y" and masukan != "n": # ketika input tidak sesuai
    sleep(0.5)
    masukan = input("apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)").lower()
  if masukan == "y":
    save(user, candi, bahan_bangunan) # memanggil fungsi save
  sleep(1)
  print("Exit berhasil")
  animasiexit()
  exit()
