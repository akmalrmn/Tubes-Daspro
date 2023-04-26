from animasi import animasiayam
from time import  sleep

def ayam_berkokok(user, idx_usn, candi):
  # Menghitung banyak candi
  banyak_candi = -1
  for element in candi :
      if element[0] != None :
          banyak_candi += 1
      else :
          break
  # Sisa candi yang perlu dibangun
  if user[idx_usn][0] == "Roro":
    if banyak_candi <= 99: # jumlah candi <= 99
      animasiayam()
      sleep(0.5)
      print("Kukuruyuk.. Kukuruyuk..")
      sleep(1)
      print(f"Jumlah Candi: {banyak_candi}")
      sleep(1)
      print()
      print("Selamat, Roro Jonggrang memenangkan permainan!")
      sleep(1.5)
      print()
      print("*Bandung Bondowoso angry noise*")
      sleep(0.5)
      print("Roro Jonggrang dikutuk menjadi candi.")
    else: # jumlah candi >= 100
      animasiayam()
      sleep(0.5)
      print("Kukuruyuk.. Kukuruyuk..")
      sleep(1)
      print(f"Jumlah Candi: {banyak_candi}")
      sleep(1.5)
      print()
      print("Yah, Bandung Bondowoso memenangkan permainan!")
    exit()
  else:
    sleep(0.5)
    print("Program ini hanya dapat diakses oleh Roro")
