def laporancandi(idx_usn,user,candi):
    if user[idx_usn][0] == "Bondowoso":
        # copas dari F06
        banyak_candi = -1
        for element in candi :
            if element[0] != None :
                banyak_candi += 1
            else :
                break
        def count_rows(arr):
            row_count = 0
            for row in arr:
                row_count += 1
            return row_count

        # banyak_pasir_digunakan didapat dari penjumlahan kolom pasir dari array candi.csv
        def banyak_pasir_digunakan():
            banyak_pasir_digunakan = 0
            for baris in candi[1:] : # memindai tiap baris dari candi tapi baris pertama gak termasuk karena baris pertama kan judul
                if baris[2] != None: # kalau belum ketemu 'None' artinya lanjut
                    banyak_pasir_digunakan += int(baris[2]) # iterasi penjumlahan pasir
                elif baris[2] == None: # kalau udah ketemu none ya berhenti
                    return(banyak_pasir_digunakan)
                    break
        # banyak_batu_digunakan didapat dari penjumlahan kolom batu dari array candi.csv
        def banyak_batu_digunakan():
            banyak_batu_digunakan = 0
            for baris in candi[1:] : # memindai tiap baris dari candi tapi baris pertama gak termasuk karena baris pertama kan judul
                if baris[3] != None: # kalau belum ketemu 'None' artinya lanjut
                    banyak_batu_digunakan += int(baris[3]) # iterasi penjumlahan batu
                elif baris[3] == None: # kalau udah ketemu none ya berhenti
                    return(banyak_batu_digunakan)
                    break

        # banyak_air_digunakan didapat dari penjumlahan kolom air dari array candi.csv
        def banyak_air_digunakan():
            banyak_air_digunakan = 0
            for baris in candi[1:] :
                if baris[4] != None:
                    banyak_air_digunakan += int(baris[4])
                elif baris[4] == None:
                    return(banyak_air_digunakan)
                    break

        def id_candi_termahal(candi):
            id_termahal = '-'
            harga_termahal = '-'
            for baris in candi[1:]:
                if baris[2] is None:
                    return f"{id_termahal} (Rp {harga_termahal})"
                    break
                else:
                    harga = 1000 * int(baris[2]) + 1500 * int(baris[3]) + 7500 * int(baris[4])
                    if harga_termahal == '-' or harga > harga_termahal:
                        harga_termahal = harga
                        id_termahal = baris[0]

        def id_candi_termurah(candi):
            id_termurah = '-'
            harga_termurah = '-'
            for baris in candi[1:]:
                if baris[2] is None:
                    return f"{id_termurah} (Rp {harga_termurah})"
                    break
                else:
                    harga = 1000 * int(baris[2]) + 1500 * int(baris[3]) + 7500 * int(baris[4])
                    if harga_termurah == '-' or harga < harga_termurah:
                        harga_termurah = harga
                        id_termurah = baris[0]
        print('Total Candi: ', banyak_candi)
        print('Total Pasir yang digunakan: ', banyak_pasir_digunakan())
        print('Total Batu yang digunakan: ', banyak_batu_digunakan())
        print('Total Air yang digunakan: ', banyak_air_digunakan())
        print(f'ID Candi Termahal: ', id_candi_termahal(candi))
        print(f'ID Candi Termurah: ', id_candi_termurah(candi))
    else:
        print('Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.')
    return idx_usn,user,candi
