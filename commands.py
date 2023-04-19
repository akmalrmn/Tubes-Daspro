from F01_login import login
from F02_logout import logout
from F07_jin_pengumpul import kumpul
from F03_summonjin import summonjin
from F04_hilangkanjin import hapus_jin

def run(masukan, login_status, idx_usn, csvlist, idx_rng, csvlist2):
    if login_status: # User sudah melakukan login
        if masukan == "login":
          print("Login gagal!")
          print(f"Anda telah login dengan username {csvlist[idx_usn][0]}, silahkan lakukan “logout” sebelum melakukan login kembali.")
        elif masukan == "logout":
          csvlist, login_status = logout(login_status, idx_usn, csvlist)
        elif masukan == "kumpul":
          csvlist = kumpul(csvlist, idx_rng)
          print(csvlist)
        elif masukan == "summonjin":
          csvlist = summonjin(csvlist, idx_usn)
        elif masukan == "hapusjin":
          csvlist, csvlist2 = hapus_jin(csvlist, csvlist2, idx_usn)
        else: # Masukan tidak sesuai dengan opsi yang ada
          print("Opsi tidak tersedia")
    elif not(login_status): # user belum melakukan login
        if masukan == "login":
          login_status, idx_usn, csvlist = login(csvlist)
        elif masukan == "logout":
          print("Logout gagal!")
          print("Anda belum login, silakan login terlebih dahulu sebelum melakukan logout!")
        else:
          print("Opsi tidak tersedia")
    return login_status, idx_usn, csvlist, idx_rng, csvlist2 # me-return beberapa variabel
