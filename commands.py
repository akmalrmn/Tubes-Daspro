from F01_login import login
from F02_logout import logout
from F07_jin_pengumpul import kumpul
from F03_summonjin import summonjin
from F04_hilangkanjin import hapus_jin
from F05_ubahjin import ubahjin
from F09_laporanjin import laporan_jin
from F15_help import Help
from F08_batch import batchbangun
from F08_batch import batchkumpul

def run(masukan, login_status, idx_usn, user, idx_rng, candi, bahan_bangunan):
    if login_status: # User sudah melakukan login
        if masukan == "login":
          login(user, login_status, idx_usn)
        elif masukan == "logout":
          user, login_status = logout(login_status, idx_usn, user)
        elif masukan == "kumpul":
          bahan_bangunan, idx_rng = kumpul(bahan_bangunan, idx_rng)
        elif masukan == "summonjin":
          user = summonjin(user, idx_usn)
        elif masukan == "hapusjin":
          user, candi = hapus_jin(user, candi, idx_usn)
        elif masukan == "ubahjin":
          user = ubahjin(user, idx_usn)
        elif masukan == "laporanjin":
          user, candi, bahan_bangunan = laporan_jin(user, candi, bahan_bangunan, idx_usn)
        elif masukan  == "help":  
          Help(login_status)
        elif masukan == "exit":
          exit()
        elif masukan == "batchkumpul":
          bahan_bangunan, idx_rng = batchkumpul(bahan_bangunan, idx_rng, user)
        elif masukan == "batchbangun":
          bahan_bangunan, idx_rng = batchbangun(idx_rng, bahan_bangunan, user)
        else: # Masukan tidak sesuai dengan opsi yang ada
          print("Opsi tidak tersedia")
    elif not(login_status): # user belum melakukan login
        if masukan == "login":
          login_status, idx_usn, user = login(user, login_status, idx_usn)
        elif masukan == "logout":
          user, login_status = logout(login_status, idx_usn, user)
        elif masukan  == "help":
          Help(login_status)
        else:
          print("Opsi tidak tersedia")
    return login_status, idx_usn, user, idx_rng, candi, bahan_bangunan # me-return beberapa variabel
