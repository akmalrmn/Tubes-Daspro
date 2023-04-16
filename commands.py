from F01_login import login
from F02_logout import logout

def run(masukan, login_status, i, user):
  if masukan == "login" and not(login_status):
    login_status, i, CSV_List = login(user)
  elif masukan == "login" and login_status:
    print("Login gagal!")
    print(f"Anda telah login dengan username {user[i][0]}, silahkan lakukan “logout” sebelum melakukan login kembali.")
  elif masukan == "logout" and login_status:
    user, login_status = logout(login_status, i, user)
  elif masukan == "logout" and not(login_status):
    print("Logout gagal!")
    print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout!")
  return login_status, i, user
