from animasi import animasiayam
from time import  sleep

def ayam_berkokok(user, idx_usn, sisa_bangun_candi):
  if user[idx_usn][0] == "Roro":
    if sisa_bangun_candi <= 99: # jumlah candi <= 99
      animasiayam()
      print("Kukuruyuk.. Kukuruyuk..")
      sleep(1)
      print(f"Jumlah Candi: {sisa_bangun_candi}")
      sleep(1)
      print("Selamat, Roro Jonggrang memenangkan permainan!")
      sleep(1.5)
      print("*Bandung Bondowoso angry noise*")
      sleep(0.5)
      print("Roro Jonggrang dikutuk menjadi candi.")
    else: # jumlah candi >= 100
      animasiayam()
      print("Kukuruyuk.. Kukuruyuk..")
      sleep(1)
      print(f"Jumlah Candi: {sisa_bangun_candi}")
      sleep(1.5)
      print("Yah, Bandung Bondowoso memenangkan permainan!")
  else:
    print("Program ini hanya dapat diakses oleh Roro")
