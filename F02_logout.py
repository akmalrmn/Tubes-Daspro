from F01_login import login

def logout():
  login_status, i, CSV_List = login()
  if login_status:
    print("Logout berhasil!")
    for j in range(i, 1000):
      CSV_List[j] = CSV_List[j+1]
    CSV_List = [row for row in CSV_List if row]
    print(CSV_List[1])
  else:
    print("Logout gagal!")
    print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout!")
