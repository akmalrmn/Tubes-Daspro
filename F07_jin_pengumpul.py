from RNG import rand_nums
from animasi import animasibahan
from time import sleep
from typing import List, Union, Tuple

def kumpul(bahan_bangunan: List[Union[str, int]], idx_rng: int, idx_usn: int, user: List[str]) -> Tuple[List[Union[str, int]], int]:
  if user[idx_usn][2] == "Pengumpul":
    increment = 0
    nama_bahan = [["pasir", 0], ["batu", 0], ["air", 0]]
    for i in range(3):
      bahan_bangunan[i+1][2] += rand_nums[idx_rng+i] # melakukan penambahan bahan dengan RNG
      nama_bahan[i][1] = rand_nums[idx_rng+i]
      bahan_bangunan[i+1][0] = nama_bahan[i][0]
    animasibahan(nama_bahan[0][1], nama_bahan[1][1], nama_bahan[2][1])
    sleep(0.5)
    print(f"{user[idx_usn][0]} menemukan", nama_bahan[0][1], "pasir,", nama_bahan[1][1], "batu, dan", nama_bahan[2][1], "air")
    idx_rng += 3
  else:
    print("Program ini hanya dapat diakses oleh jin Pengumpul")
  return bahan_bangunan, idx_rng