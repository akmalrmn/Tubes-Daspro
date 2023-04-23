from time import sleep

def laporan_jin(user, candi, bahan_bangunan, idx_usn):

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
            if x[i][2] == "Pengumpul":
                jumlah += 1
            else:
                continue
        return jumlah

    def total_jin_pembangun(x):
        jumlah = 0
        for i in range (panjang(x)):
            if x[i][2] == "Pembangun":
                jumlah += 1
            else:
                continue
        return jumlah

    def jin_terajin(x,y):
        
        arr_jin_pembangun = [None for i in range (total_jin_pembangun(x))]
        j = 0
        for i in range (panjang(x)):
            if x[i][2] == "pembangun":
                arr_jin_pembangun[j] = x[i][0]
                j += 1
        
        total = 0
        rajin = "-"
        nama_jin = ""
        if y[1][0] == None:
            if panjang(x) == 3:
                return rajin
            else:
                rajin = arr_jin_pembangun[0]
                for i in range (1, total_jin_pembangun(x)):
                    if arr_jin_pembangun[i] < rajin:
                        rajin = arr_jin_pembangun[i]
                return rajin

        else:
            for i in range (3, panjang(x)):
                if x[i][2] == "pembangun":
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

        arr_jin_pembangun = [None for i in range (total_jin_pembangun(x))]
        j = 0
        for i in range (panjang(x)):
            if x[i][2] == "pembangun":
                arr_jin_pembangun[j] = x[i][0]
                j += 1
        
        total = 101
        malas = "-"
        nama_jin = ""
        if y[1][0] == None:
            if panjang(x) == 3:
                return malas
            else:
                malas = arr_jin_pembangun[0]
                for i in range (1, total_jin_pembangun(x)):
                    if arr_jin_pembangun[i] > malas:
                        malas = arr_jin_pembangun[i]
                return malas
        
        else:
            for i in range (3, panjang(x)):
                if x[i][2] == "pembangun":
                    nama_jin = x[i][0]
                    total_sementara = 0
                    for j in range (panjang(y)):
                        if y[j][1] == nama_jin:
                            total_sementara += 1
                        else:
                            continue
                    if total_sementara < total:
                        total = total_sementara
                        malas = nama_jin
                    elif total_sementara == total:
                        if malas > nama_jin:
                            malas = malas
                        else:
                            malas = nama_jin
                    else:
                        continue
            return malas

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
    if user[idx_usn][0] == "Bondowoso":
        sleep(1)
        print(f"> Total Jin: {total_jin(user)}")
        print(f"> Total Jin Pengumpul: {total_jin_pengumpul(user)}")
        print(f"> Total Jin Pembangun: {total_jin_pembangun(user)}")
        print(f"> Jin Terajin: {jin_terajin(user,candi)}")
        print(f"> Jin Termalas: {jin_termalas(user,candi)}")
        print(f"> Jumlah Pasir: {jumlah_pasir(bahan_bangunan)} unit")
        print(f"> Jumlah Air: {jumlah_air(bahan_bangunan)} unit")
        print(f"> Jumlah Batu: {jumlah_batu(bahan_bangunan)} unit")
    else:
      print("Program ini hanya dapat diakses oleh Bondowoso")
    return user, candi, bahan_bangunan
