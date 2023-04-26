# import program
from F01_login import login
from F02_logout import logout
from F07_jin_pengumpul import kumpul
from F03_summonjin import summonjin
from F04_hilangkanjin import hapus_jin
from F05_ubahjin import ubahjin
from F09_laporanjin import laporan_jin
from F15_help import Help
from F08_batch import batchbangun, batchkumpul
from F11_hancurkan_candi import hancurkan_candi
from F06_jin_pembangun import jin_pembangun
from F12_ayam_berkokok import ayam_berkokok
from F16_exitt import exitt
from F14_save import save
from F10_laporancandi import laporancandi

def run(masukan, login_status, idx_usn, user, idx_rng, candi, idx_rng2, bahan_bangunan):
    if login_status: # User sudah melakukan login
        if masukan == "login":
          login(user, login_status, idx_usn)
        elif masukan == "logout":
          user, login_status = logout(login_status, idx_usn, user)
        elif masukan == "kumpul":
          bahan_bangunan, idx_rng = kumpul(bahan_bangunan, idx_rng, idx_usn, user)
        elif masukan == "summonjin":
          user = summonjin(user, idx_usn)
        elif masukan == "hapusjin":
          user, candi = hapus_jin(user, candi, idx_usn)
        elif masukan == "ubahjin":
          user = ubahjin(user, idx_usn)
        elif masukan == "laporanjin":
          user, candi, bahan_bangunan = laporan_jin(user, candi, bahan_bangunan, idx_usn)
        elif masukan  == "help":  
          Help(login_status, idx_usn, user)
        elif masukan == "exit":
          exitt(user, candi, bahan_bangunan)
        elif masukan == "batchkumpul":
          bahan_bangunan, idx_rng = batchkumpul(bahan_bangunan, idx_rng, user, idx_usn)
        elif masukan == "batchbangun":
          bahan_bangunan, idx_rng, candi = batchbangun(idx_rng2, bahan_bangunan, user, idx_usn, candi)
        elif masukan == "hancurkancandi":
          candi = hancurkan_candi(candi, idx_usn, user)
        elif masukan == "bangun":
          idx_rng, bahan_bangunan, candi, user = jin_pembangun(idx_rng, bahan_bangunan, candi, user, idx_usn)
        elif masukan == "ayamberkokok":
          ayam_berkokok(user, idx_usn, candi)
        elif masukan == "save":
          save(user, candi, bahan_bangunan)
        elif masukan == "laporancandi":
          laporancandi(idx_usn, user, candi)
        else: # Masukan tidak sesuai dengan opsi yang ada
          print(f"Opsi {masukan} tidak tersedia")
    elif not(login_status): # user belum melakukan login
        if masukan == "login":
          login_status, idx_usn, user = login(user, login_status, idx_usn)
        elif masukan == "logout":
          user, login_status = logout(login_status, idx_usn, user)
        elif masukan  == "help":
          Help(login_status, idx_usn, user)
        elif masukan == "save":
          save(user, candi, bahan_bangunan)
        else: # Masukan tidak sesuai dengan opsi yang ada
          print(f"Opsi {masukan} tidak tersedia")
    return login_status, idx_usn, user, idx_rng, candi, idx_rng2, bahan_bangunan # me-return beberapa variabel
