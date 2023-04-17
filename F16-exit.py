def exit():
  masukan = input("pakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)").lower()
  while masukan != "y" and masukan != "n":
    masukan = input("pakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)").lower()
  if masukan == "y":
    save()
  else:
    nosave = True
  return nosave