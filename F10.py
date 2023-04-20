import csvtolist

# Convert array dari csv
arr_candi = csvtolist.csv_to_list('candi.csv',101,5)

def count_rows(arr):
    row_count = 0
    for row in arr:
        row_count += 1
    return 

# copas dari F06
banyak_candi = -1
for element in arr_candi :
    if element[0] != None :
        banyak_candi += 1
    else :
        break

# banyak_pasir_digunakan didapat dari penjumlahan kolom pasir dari array candi.csv
def banyak_pasir_digunakan():
    banyak_pasir_digunakan = 0
    for baris in arr_candi[1:] : # memindai tiap baris dari arr_candi tapi baris pertama gak termasuk karena baris pertama kan judul
        if baris[2] != 'None': # kalau belum ketemu 'None' artinya lanjut
            banyak_pasir_digunakan += baris[2] # iterasi penjumlahan pasir
        elif baris[2] == 'None': # kalau udah ketemu none ya berhenti
            print(banyak_pasir_digunakan)
            break
# banyak_batu_digunakan didapat dari penjumlahan kolom batu dari array candi.csv
def banyak_batu_digunakan():
    banyak_batu_digunakan = 0
    for baris in arr_candi[1:] : # memindai tiap baris dari arr_candi tapi baris pertama gak termasuk karena baris pertama kan judul
        if baris[3] != 'None': # kalau belum ketemu 'None' artinya lanjut
            banyak_batu_digunakan += baris[3] # iterasi penjumlahan batu
        elif baris[3] == 'None': # kalau udah ketemu none ya berhenti
            print(banyak_batu_digunakan)
            break

# banyak_air_digunakan didapat dari penjumlahan kolom air dari array candi.csv
def banyak_air_digunakan():
    banyak_air_digunakan = 0
    for baris in arr_candi[1:] :
        if baris[4] != 'None':
            banyak_air_digunakan += baris[4]
        elif baris[4] == 'None':
            print(banyak_air_digunakan)
            break

def hargacandi():
    
    return harga_candi

arr_harga = []
for baris in arr_candi:
    harga = 1000 * baris[2] + 1500 * baris[3] + 7500 * baris[4] # harga = 1000 * Pasir + 1500 * Batu + 7500 * Air
    arr_harga.append(harga)
candi_termahal = max(arr_harga)
candi_termurah = min(arr_harga)

def laporancandi():
    if username == 'Bondowoso':
        print('Total Candi: ', banyak_candi)
        print('Total Pasir yang digunakan: ', banyak_pasir_digunakan())
        print('Total Batu yang digunakan: ', banyak_batu_digunakan())
        print('Total Air yang digunakan: ', banyak_air_digunakan())
        print('ID Candi Termahal: ', candi_termahal)
        print('ID Candi Termurah: ', candi_termurah)
    else:
        print('Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.')
