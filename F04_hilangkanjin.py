def hapus_jin(user, candi, idx_usn):
    import csvtolist

    # fungsi buat hitung len array
    def panjang_array(array):
        i = 0
        while True:
            if array[i][0] == None:
                break
            else:
                i += 1
        return i

    # fungsi hapus jin
    def hapus_jin(nama_jin,array_user):
        for i in range (panjang_array(array_user)):
            if nama_jin == array_user[i][0]:
                array_user[i][0] = ""
        return array_user

    # fungsi hapus candi
    def hapus_candi_jin(nama_jin,array_candi):
        for i in range (panjang_array(array_candi)):
            if nama_jin == array_candi[i][1]:
                array_candi[i][1] = ""
        return array_candi

    # habis dihapus, data yang dikanannya geser ke kiri
    # contoh [1,"",3,None] --> [1,3,None]
    def geser_arr_user(array_user):
        arr = [[None for _ in range(3)] for _ in range (1001)]
        j = 0
        for i in range (panjang_array(array_user)):
            if array_user[i][0] != "":
                arr[j] = array_user[i]
                j += 1
        return arr

    # habis dihapus, data yang dikanannya geser ke kiri
    # contoh [1,"",3,None] --> [1,3,None]
    def geser_arr_candi(array_candi):
        arr = [[None for _ in range(5)] for _ in range (101)]
        j = 0
        for i in range (panjang_array(array_candi)):
            if array_candi[i][1] != "":
                arr[j] = array_candi[i]
                j += 1
        return arr
    
    # fungsi buat bikin array gaada None-nya
    # contoh yang awalnya [1,2,3,None] --> jadi [1,2,3]
    def array_bersih(array):
        arr = [None for i in range (panjang_array(array))]
        for i in range (panjang_array(array)):
            arr[i] = array[i]
        return arr

    if user[idx_usn][0] == "Bondowoso":
      jin = input("Masukkan username jin: ")
      for i in range (panjang_array(user)):
          if jin == user[i][0]:
              confirm = input(f"Apakah anda yakin ingin menghapus jin dengan username {jin} (Y/N)? ")
              if confirm == "Y":
                  user = geser_arr_user(hapus_jin(jin, user))
                  candi = geser_arr_candi(hapus_candi_jin(jin, candi))
                  print("Jin telah berhasil dihapus dari alam gaib.")
                  break
              else:
                  print("okede, sip")
                  break
      else:
          print("Tidak ada jin dengan username tersebut.")
    else:
      print("Program ini hanya dapat diakses oleh Bondowoso")
    return user, candi
