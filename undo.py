import csvtolist

def undo(candi, idx_usn, user, bahan_bangunan):

    # fungsi hitung banyak candi yang dibangun oleh jin
    def hitung_candi(arr_file_candi,nama_jin):
        sum = 0
        for candi in arr_file_candi:
            if candi[1] == nama_jin:
                sum += 1
        return sum
    
    # fungsi cari candi yang hilang
    def cari_candi_hilang(arr_file_candi,nama_jin):
        candi_hilang = [None for i in range (hitung_candi(arr_file_candi,nama_jin))]
        idx = 0
        for candi in arr_file_candi:
            if candi[1] == nama_jin :
                candi_hilang[idx] = candi
                idx += 1
        return candi_hilang

    # fungsi cari jin yang hilang
    def cari_jin_hilang(user, arr_file_user):
        idx = 0
        loop = True
        while loop:
            if user[idx] != arr_file_user[idx] and user[idx] != None:
                loop = False
            idx += 1
        jin_hilang = arr_file_user[idx]
        return jin_hilang
    
    # fungsi mengurangi bahan bangunan untuk membuat candi
    def bangun_ulang_candi(bahan_bangunann,candi_hilang):
        for candi in candi_hilang:
            bahan_bangunan[1][2] -= candi[2]
            bahan_bangunan[2][2] -= candi[3]
            bahan_bangunan[3][2] -= candi[4]
        
    # fungsi susun array user
    def susun_array_user(user,jin_hilang):
        idx = 0
        loop = True 
        while loop :
            if user[idx][0] == None :
                user[idx] = jin_hilang
                loop = False
            idx += 1
        return user

    # fungai susun array candi
    def susun_array_candi(candi,candi_hilang):
        # hitung banyak candi yang hilang
        banyak_candi_hilang = 0
        for i in candi_hilang :
            banyak_candi_hilang += 1
        idx = 0
        loop = True
        idx_candi_hilang = 0
        while loop:
            if idx_candi_hilang == banyak_candi_hilang - 1:
                loop = False 
            if candi[idx][0] == None:
                candi[idx] = candi_hilang[idx_candi_hilang]
                idx_candi_hilang += 1
                idx += 1
            idx += 1
        return candi
        
    # Algoritma
    if user[idx_usn][0] == "Bondowoso":
        jin_hilang = cari_jin_hilang(user,arr_file_user)
        nama_jin = jin_hilang[0]
        candi = susun_array_candi(candi,cari_candi_hilang(arr_file_candi,nama_jin))
        user = susun_array_user(user,cari_jin_hilang(user,arr_file_user))
        bangun_ulang_candi(bahan_bangunan,cari_candi_hilang(arr_file_candi,nama_jin))
        print('Anda berhasil melakukan undo hilangkan jin')
    else :
        print("Program ini hanya dapat di akses oleh bondowoso")
    
    return candi,user
