def hapus_jin():
    import csvtolist

    # Convert array dari csv
    arr_candi = csvtolist.csv_to_list('candi.csv',101,5)
    arr_user = csvtolist.csv_to_list('user.csv',1003,3)

    def panjang(x):
        i = 0
        while True:
            if x[i][0] == None:
                break
            else:
                i += 1
        return i

    def hapus_jin(x,y):
        for i in range (panjang(y)):
            if x == y[i][0]:
                y[i][0] = ""
        return y

    def hapus_candi_jin(x,y):
        for i in range (panjang(y)):
            if x == y[i][1]:
                y[i][1] = ""
        return y

    def geser_arr_user(x):
        arr = [[None for _ in range(3)] for _ in range (1003)]
        j = 0
        for i in range (panjang(x)):
            if x[i][0] != "":
                arr[j] = x[i]
                j += 1
        return arr

    def geser_arr_candi(x):
        arr = [[None for _ in range(5)] for _ in range (101)]
        j = 0
        for i in range (panjang(x)):
            if x[i][1] != "":
                arr[j] = x[i]
                j += 1
        return arr

    def bersih(x):
        arr = [None for i in range (panjang(x))]
        for i in range (panjang(x)):
            arr[i] = x[i]
        return arr

    jin = input("Masukkan username jin: ")
    for i in range (panjang(arr_user)):
        if jin == arr_user[i][0]:
            confirm = input(f"Apakah anda yakin ingin menghapus jin dengan username {jin} (Y/N)? ")
            break
    else:
        print("Tidak ada jin dengan username tersebut.")

    if confirm == "Y":
        arr_user = bersih(geser_arr_user(hapus_jin(jin, arr_user)))
        arr_candi = bersih(geser_arr_candi(hapus_candi_jin(jin, arr_candi)))
        print("Jin telah berhasil dihapus dari alam gaib.")

hapus_jin()