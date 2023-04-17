from F01_login import login
from F02_logout import logout
from F07_jin_pengumpul import kumpul

def run(masukan, login_status, idx_usn, csvlist, idx_rng):
    if login_status:
        if masukan == "login":
          print("Login gagal!")
          print(f"Anda telah login dengan username {csvlist[idx_usn][0]}, silahkan lakukan “logout” sebelum melakukan login kembali.")
        elif masukan == "logout":
          csvlist, login_status = logout(login_status, idx_usn, csvlist)
        elif masukan == "kumpul":
          csvlist = kumpul(csvlist, idx_rng)
          print(csvlist)
        else:
          print("Opsi tidak tersedia")
    elif not(login_status):
        if masukan == "login":
          login_status, idx_usn, csvlist = login(csvlist)
        elif masukan == "logout":
          print("Logout gagal!")
          print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout!")
        else:
          print("Opsi tidak tersedia")
    return login_status, idx_usn, csvlist, idx_rng
