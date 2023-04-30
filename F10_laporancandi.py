from time import sleep
from typing import Tuple, List, Union

def laporancandi(idx_usn: int, user: List[str], candi: List[Union[str, int]]) -> Tuple[int, List[str], List[Union[str, int]]]:
    if user[idx_usn][0] == "Bondowoso":
        # menghitung banyak candi
        i = 0
        while True:
            if candi[i][0] == None:
                break
            else:
                i += 1
        banyak_candi = i -1
        # menghitung panjang array
        def count_rows(arr: List[Union[str, int]]) -> int:
            panjang = 0
            while True:
                if arr[panjang][0] == None:
                    break
                else:
                    panjang += 1
            return panjang

        # banyak_pasir_digunakan didapat dari penjumlahan kolom pasir dari array candi.csv
        def banyak_pasir_digunakan() -> int:
            banyak_pasir_digunakan = 0
            for i in range(1, count_rows(candi)) : # memindai tiap baris dari candi tapi baris pertama gak termasuk karena baris pertama kan judul
                baris = candi[i]
                if baris[2] is not None: # kalau belum ketemu 'None' artinya lanjut
                    banyak_pasir_digunakan += int(baris[2]) # iterasi penjumlahan pasir
                else: # kalau udah ketemu none ya berhenti
                    break
            return(banyak_pasir_digunakan)
                    
        # banyak_batu_digunakan didapat dari penjumlahan kolom batu dari array candi.csv
        def banyak_batu_digunakan() -> int:
            banyak_batu_digunakan = 0
            for i in range(1, count_rows(candi)):
                baris = candi[i]
                if baris[3] is not None:
                    banyak_batu_digunakan += int(baris[3])
                else:
                    break
            return banyak_batu_digunakan

        # banyak_air_digunakan didapat dari penjumlahan kolom air dari array candi.csv
        def banyak_air_digunakan() -> int:
            banyak_air_digunakan = 0
            for i in range(1, count_rows(candi)) :
                baris = candi[i]
                if baris[4] is not None:
                    banyak_air_digunakan += int(baris[4])
                else:
                    break
            return banyak_air_digunakan

        def id_candi_termahal(candi: List[Union[str, int]]) -> int:
            id_termahal = '-'
            harga_termahal = '-'
            for i in range(1, count_rows(candi)):
                baris = candi[i] # mengambil 1 candi untuk dibandingkan
                if baris[2] is None: # tidak ada candi lagi
                    return f"{id_termahal} (Rp {harga_termahal})"
                    break
                else:
                    harga = 1000 * int(baris[2]) + 1500 * int(baris[3]) + 7500 * int(baris[4]) # rumus harga candi
                    if harga_termahal == '-' or harga > harga_termahal:
                        harga_termahal = harga
                        id_termahal = baris[0]
            return id_termahal

        def id_candi_termurah(candi: List[Union[str, int]]) -> int:
            id_termurah = '-'
            harga_termurah = '-'
            for i in range(1, count_rows(candi)):
                baris = candi[i] # mengambil 1 candi untuk dibandingkan
                if baris[2] is None:
                    return f"{id_termurah} (Rp {harga_termurah})"
                    break
                else:
                    harga = 1000 * int(baris[2]) + 1500 * int(baris[3]) + 7500 * int(baris[4])
                    if harga_termurah == '-' or harga < harga_termurah: # mencari harga termahal
                        harga_termurah = harga
                        id_termurah = baris[0]
            return id_termurah
        sleep(0.5)
        print('Total Candi: ', banyak_candi)
        print('Total Pasir yang digunakan: ', banyak_pasir_digunakan())
        print('Total Batu yang digunakan: ', banyak_batu_digunakan())
        print('Total Air yang digunakan: ', banyak_air_digunakan())
        print(f'ID Candi Termahal: ', id_candi_termahal(candi))
        print(f'ID Candi Termurah: ', id_candi_termurah(candi))
    else:
        sleep(0.5)
        print('Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.')
    return idx_usn,user,candi
# Aplikasi
#username = 'Bondowoso'
#laporancandi()