from RNG import rand_nums2
import random
from time import sleep
from animasi import animasicandi

def jin_pembangun(idx_rng, bahan_bangunan, candi, user, idx_usn):
    # Menghitung banyak candi
    banyak_candi = -1
    for element in candi :
        if element[0] != None :
            banyak_candi += 1
        else :
            break
    # Sisa candi yang perlu dibangun
    sisa_bangun_candi = 100 - banyak_candi
    if user[idx_usn][2] == "Pembangun":
        if bahan_bangunan[1][2] != None and bahan_bangunan[2][2] != None and bahan_bangunan[3][2] != None:
            pembuat = user[idx_usn]

            # idd dari candi yang dibangun
            idd = 1
            if candi[1][0] != None :
                for i in range (101):
                    if candi[i][0] == None :
                        idd = int(candi[i-1][0]) + 1
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

            # Algoritma
            if sisa_pasir < 0 or sisa_batu < 0 or sisa_air < 0 :
                sleep(0.5)
                print('Bahan bangunan tidak mencukupi.\nCandi tidak bisa dibangun!')
            else :
                animasicandi()
                if banyak_candi == 100 :
                    sleep(1)
                    print('Candi berhasil dibangun.\nSisa candi yang perlu dibangun: 0.')
                else :
                    sisa_bangun_candi -= 1
                    sleep(1)
                    print(f'Candi berhasil dibangun.\nSisa candi yang perlu dibangun: {sisa_bangun_candi}.')

                # Mengubah jumlah pasir,batu,dan air, pada array bahan_bangunan karena candi berhasil dibangun
                bahan_bangunan[1][2] = sisa_pasir
                bahan_bangunan[2][2] = sisa_batu
                bahan_bangunan[3][2] = sisa_air
            
            # Membuat array untuk ditambahkan ke dalam file
            if banyak_candi < 100 :
                # Menggabungkan list ke dalam file candi
                candii_baru = [idd,pembuat[0],pasir_dibutuhkan,batu_dibutuhkan,air_dibutuhkan]
                idx = 0
                while idx < 101 :
                    if candi[idx][0] == None:
                        candi[idx] = candii_baru
                        idx = 101
                    idx += 1

            # Jika banyak candi sudah 100 maka candi yang sudah dibuat tidak disimpan
            else :
                candii_baru = candi
        else:
            sleep(0.5)
            print('Bahan bangunan tidak mencukupi.\nCandi tidak bisa dibangun!')
    else :
        candii_baru = candi
        sleep(0.5)
        print("Program ini hanya dapat diakses oleh jin pembangun")
    return idx_rng, bahan_bangunan, candi, user