import numpy as np
from RNG import rand_nums2

def jin_pembangun(idx_rng, bahan_bangunan, candi, user):
    # Id dari candi yang dibangun
    id = 1
    for i in range (101):
        if candi[i][0] == None and i != 1:
            id = int(candi[i-1][0]) + 1
            break

    # Menghitung banyak candi
    banyak_candi = -1
    for element in candi :
        if element[0] != None :
            banyak_candi += 1
        else :
            break

    # Bahan bangunan yang dibutuhkan
    pasir_dibutuhkan = rand_nums2[idx_rng]
    batu_dibutuhkan = rand_nums2[idx_rng+1]
    air_dibutuhkan = rand_nums2[idx_rng+2]
    idx_rng += 3

    # Sisa bahan bangunan yang sudah dipakai
    sisa_pasir = int(bahan_bangunan[1][2]) - pasir_dibutuhkan
    sisa_batu = int(bahan_bangunan[2][2]) - batu_dibutuhkan
    sisa_air = int(bahan_bangunan[3][2]) - air_dibutuhkan

    # Menghitung banyak jin pembangun dalam array user
    banyak_jin_pembangun = 0
    for user in user :
        if user[2] == "jin_pembangun" :
            banyak_jin_pembangun += 1

    # List nama jin pembangun candi
    nama_jin = [None for i in range (banyak_jin_pembangun)]
    idx = 0
    for baris in user :
        if baris is None:
            return 0
        elif baris[2] == "jin_pembangun" :
            nama_jin[idx] = baris[0]
            idx += 1
    
    # Mengambil nama jin random dari list nama_jin
    random_index = np.random.randint(banyak_jin_pembangun)
    pembuat = nama_jin[random_index]

    # Sisa candi yang perlu dibangun
    sisa_bangun_candi = 99 - banyak_candi

    # Algoritma
    if sisa_pasir < 0 or sisa_batu < 0 or sisa_air < 0 :
        print('Bahan bangunan tidak mencukupi.\nCandi tidak bisa dibangun!')
    else :
        if banyak_candi == 100 :
            print('Candi berhasil dibangun.\nSisa candi yang perlu dibangun: 0.')
            bahan_bangunan[1][2] = sisa_pasir
            bahan_bangunan[2][2] = sisa_batu
            bahan_bangunan[3][2] = sisa_air
        else :
            print(f'Candi berhasil dibangun.\nSisa candi yang perlu dibangun: {sisa_bangun_candi}.')
            bahan_bangunan[1][2] = sisa_pasir
            bahan_bangunan[2][2] = sisa_batu
            bahan_bangunan[3][2] = sisa_air
    


    # Membuat array untuk ditambahkan ke dalam file
    if banyak_candi < 100 :
        # Menggabungkan list ke dalam file candi
        candii_baru = [id,pembuat,pasir_dibutuhkan,batu_dibutuhkan,air_dibutuhkan]
        with open('candi.csv', 'a') as file:
            row = ''
            for item in candii_baru:
                row += str(item) + ';'
            file.write(row[:-1] + '\n')

    return idx_rng, bahan_bangunan, candii_baru, user
