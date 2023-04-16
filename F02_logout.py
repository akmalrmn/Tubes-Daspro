from F01_login import login

def logout(login_status, i, CSV_List):
  print("Logout berhasil!")
  for j in range(i, 1000):
    CSV_List[j] = CSV_List[j+1]
  CSV_List = [row for row in CSV_List if row]
  login_status = False
  return CSV_List, login_status
