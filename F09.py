def laporan_jin():
    import csvtolist

    # Convert array dari csv
    arr_candi = csvtolist.csv_to_list('candi.csv',101,5)
    arr_user = csvtolist.csv_to_list('user.csv',1003,3)
    arr_bahan_bangunan = csvtolist.csv_to_list('bahan_bangunan.csv',101,3)

    def panjang(x):
        i = 0
        while True:
            if x[i][0] == None:
                break
            else:
                i += 1
        return i

    def total_jin(x):
        jumlah = 0
        for i in range (panjang(x)):
            if x[i][0] == "Bondowoso" or x[i][0] == "Roro" or x[i][0] == "username":
                continue
            else:
                jumlah += 1
        return jumlah

    def total_jin_pengumpul(x):
        jumlah = 0
        for i in range (panjang(x)):
            if x[i][2] == "pengumpul":
                jumlah += 1
            else:
                continue
        return jumlah

    def total_jin_pembangun(x):
        jumlah = 0
        for i in range (panjang(x)):
            if x[i][2] == "pembangun":
                jumlah += 1
            else:
                continue
        return jumlah

    def jin_terajin(x,y):
        total = 0
        rajin = "-"
        nama_jin = ""
        if y[1][0] == None:
            return rajin
        else:
            for i in range (3, panjang(x)):
                nama_jin = x[i][0]
                total_sementara = 0
                for j in range (panjang(y)):
                    if y[j][1] == nama_jin:
                        total_sementara += 1
                    else:
                        continue
                if total_sementara > total:
                    total = total_sementara
                    rajin = nama_jin
                elif total_sementara == total:
                    if rajin > nama_jin:
                        rajin = nama_jin
                    else:
                        rajin = rajin
                else:
                    continue
            return rajin

    def jin_termalas(x,y):
        total = 101
        rajin = "-"
        nama_jin = ""
        if y[1][0] == None:
            return rajin
        else:
            for i in range (3, panjang(x)):
                nama_jin = x[i][0]
                total_sementara = 0
                for j in range (panjang(y)):
                    if y[j][1] == nama_jin:
                        total_sementara += 1
                    else:
                        continue
                if total_sementara < total:
                    total = total_sementara
                    rajin = nama_jin
                elif total_sementara == total:
                    if rajin > nama_jin:
                        rajin = rajin
                    else:
                        rajin = nama_jin
                else:
                    continue
            return rajin

    def jumlah_pasir(x):
        jumlah = 0
        for i in range (panjang(x)):
            if x[i][0] == "pasir":
                jumlah += int(x[i][2])
            else:
                continue
        return jumlah

    def jumlah_air(x):
        jumlah = 0
        for i in range (panjang(x)):
            if x[i][0] == "air":
                jumlah += int(x[i][2])
            else:
                continue
        return jumlah

    def jumlah_batu(x):
        jumlah = 0
        for i in range (panjang(x)):
            if x[i][0] == "batu":
                jumlah += int(x[i][2])
            else:
                continue
        return jumlah

    print(">>> laporanjin")

    print(f"> Total Jin: {total_jin(arr_user)}")
    print(f"> Total Jin Pengumpul: {total_jin_pengumpul(arr_user)}")
    print(f"> Total Jin Pembangun: {total_jin_pembangun(arr_user)}")
    print(f"> Jin Terajin: {jin_terajin(arr_user,arr_candi)}")
    print(f"> Jin Termalas: {jin_termalas(arr_user,arr_candi)}")
    print(f"> Jumlah Pasir: {jumlah_pasir(arr_bahan_bangunan)} unit")
    print(f"> Jumlah Air: {jumlah_air(arr_bahan_bangunan)} unit")
    print(f"> Jumlah Batu: {jumlah_batu(arr_bahan_bangunan)} unit")

laporan_jin()