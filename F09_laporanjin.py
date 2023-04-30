from time import sleep
from typing import Tuple, List, Union

def laporan_jin(user: List[str], candi: List[Union[str, int]], bahan_bangunan: List[Union[str, int]], idx_usn: int) -> Tuple[List[str], List[Union[str, int]], List[Union[str, int]]]:
    # fungsi untuk mencari panjang array
    def panjang(x: List[Union[str, int]]) -> int:
        i = 0
        while True:
            if x[i][0] == None:
                break
            else:
                i += 1
        return i

    def total_jin(x: List[str]) -> int:
        jumlah = 0
        for i in range (panjang(x)):
            if x[i][0] == "Bondowoso" or x[i][0] == "Roro" or x[i][0] == "username":
                continue
            else:
                jumlah += 1
        return jumlah

    def total_jin_pengumpul(x: List[str]) -> int:
        jumlah = 0
        for i in range (panjang(x)):
            if x[i][2] == "Pengumpul":
                jumlah += 1
            else:
                continue
        return jumlah

    def total_jin_pembangun(x: List[str]) -> int:
        jumlah = 0
        for i in range (panjang(x)):
            if x[i][2] == "Pembangun":
                jumlah += 1
            else:
                continue
        return jumlah

    def jin_terajin(y: List[Union[str, int]]) -> str:
        total = 0
        rajin = "-"
        nama_jin = ""
        if y[1][0] == None: # tidak ada jin
            return rajin
        
        else:
            for i in range (1, panjang(y)): 
                nama_jin = y[i][1] # mengambil 1 nama jin dari list candi
                total_sementara = 0
                for j in range (1, panjang(y)): # mengecek apabila ada nama yg sama di list candi
                    if y[j][1] == nama_jin:
                        total_sementara += 1
                    else:
                        continue
                if total_sementara > total: # membandingkan jumlah nama yg muncul
                    total = total_sementara
                    rajin = nama_jin
                elif total_sementara == total:
                    if rajin > nama_jin: # mengurutkan secara leksikografis
                        rajin = nama_jin
                    else:
                        rajin = rajin
                else: # total sementara kurang dari total
                    continue
            return rajin
        
    def jin_termalas(y: List[Union[str, int]]) -> str:
        total = 101
        malas = "-"
        nama_jin = ""
        if y[1][0] == None: # tidak ada jin
            return malas
        
        else:
            for i in range (1, panjang(y)):
                nama_jin = y[i][1] # mengambil 1 nama dari list candi
                total_sementara = 0
                for j in range (1, panjang(y)): # mengecek apabila ada nama yg sama di list candi
                    if y[j][1] == nama_jin:
                        total_sementara += 1
                    else:
                        continue
                if total_sementara == 0:
                    continue
                elif total_sementara < total: # membandingkan jumlah nama yg muncul
                    total = total_sementara
                    malas = nama_jin
                elif total_sementara == total:
                    if malas > nama_jin: # mengurutkan secara leksikografis
                        malas = malas
                    else:
                        malas = nama_jin
                else:  # total sementara kurang dari total
                    continue
            return malas
    # menghitung jumlah bahan
    def jumlah_pasir(x: List[Union[str, int]]) -> int:
        jumlah = 0
        for i in range (panjang(x)):
            if x[i][0] == "pasir":
                jumlah += int(x[i][2])
            else:
                continue
        return jumlah

    def jumlah_air(x: List[Union[str, int]]) -> int:
        jumlah = 0
        for i in range (panjang(x)):
            if x[i][0] == "air":
                jumlah += int(x[i][2])
            else:
                continue
        return jumlah

    def jumlah_batu(x: List[Union[str, int]]) -> int: 
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
        print(f"> Jin Terajin: {jin_terajin(candi)}")
        print(f"> Jin Termalas: {jin_termalas(candi)}")
        print(f"> Jumlah Pasir: {jumlah_pasir(bahan_bangunan)} unit")
        print(f"> Jumlah Air: {jumlah_air(bahan_bangunan)} unit")
        print(f"> Jumlah Batu: {jumlah_batu(bahan_bangunan)} unit")
    else: # bukan bondowoso
      print("Program ini hanya dapat diakses oleh Bondowoso")
    return user, candi, bahan_bangunan