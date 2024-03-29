from RNG import rand_nums, rand_nums2
from animasi import animasibahan, animasicandi
from typing import List, Union, Tuple

def batchkumpul(arr_bahan_bangunan: List[Union[str, int]], idx_rng: int, arr_user: List[str], idx_usn: int) -> Tuple[List[Union[str, int]], int]:
    if arr_user[idx_usn][0] == "Bondowoso":
        banyak_jin_pengumpul = 0
        pasir_dikumpul = 0
        batu_dikumpul = 0
        air_dikumpul = 0
        k = 0
        while True:
            if arr_user[k][0] == None:
                break
            elif arr_user[k][2] == "Pengumpul":
                banyak_jin_pengumpul += 1
                k += 1
            else:
                k += 1
        if banyak_jin_pengumpul > 0:
            for i in range(banyak_jin_pengumpul):
                pasir_dikumpul += rand_nums[idx_rng]
                batu_dikumpul += rand_nums[idx_rng+1]
                air_dikumpul += rand_nums[idx_rng+2]
                idx_rng += 3
            print(
                f"Mengerahkan {banyak_jin_pengumpul} jin untuk mengumpulkan bahan.")
            animasibahan(pasir_dikumpul, batu_dikumpul, air_dikumpul)
            print(
                f"Jin menemukan total {pasir_dikumpul} pasir, {batu_dikumpul} batu, dan {air_dikumpul} air.")
            arr_bahan_bangunan[1][2] += pasir_dikumpul
            arr_bahan_bangunan[2][2] += batu_dikumpul
            arr_bahan_bangunan[3][2] += air_dikumpul
        else:
            print(
                "Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    else:
        print("Program ini hanya dapat diakses oleh Bondowoso")
    return arr_bahan_bangunan, idx_rng


def batchbangun(idx_rng2: int, arr_bahan_bangunan: List[Union[str, int]], arr_user: List[str], idx_usn: int, candi: List[Union[str, int]]) -> Tuple[List[Union[str, int]], int, List[Union[str, int]]]:
    if arr_user[idx_usn][0] == "Bondowoso":
        banyak_jin_pembangun, pasirtotal, batutotal, airtotal, pasir, batu, air = 0, 0, 0, 0, list(), list(), list()
        k = 0
        banyak_jin_pembangun = 0
        while True:
            if arr_user[k][0] == None:
                break
            elif arr_user[k][2] == "Pembangun":
                banyak_jin_pembangun += 1
                k += 1
            else:
                k += 1
        list_pembangun = [None for i in range(banyak_jin_pembangun)]
        z = 0
        g = 0
        while True:
            if arr_user[z][0] == None:
                break
            elif arr_user[z][2] == "Pembangun":
                list_pembangun[g] = arr_user[z][0]
                g += 1
                z += 1
            else:
                z += 1
        if banyak_jin_pembangun > 0:  # jika terdapat jin pembangun
            j = 0
            while True:
                if candi[j][0] == None:
                    break
                else:
                    j += 1
            pasir = [0 for i in range(banyak_jin_pembangun)]
            batu = [0 for i in range(banyak_jin_pembangun)]
            air = [0 for i in range(banyak_jin_pembangun)]
            pasirtotal = 0
            batutotal = 0
            airtotal = 0

            # loop jumlah jin untuk mengetahui jumlah bahan dibutuhkan
            for i in range(banyak_jin_pembangun):
                pasir[i] = rand_nums2[idx_rng2]
                batu[i] = rand_nums2[idx_rng2+1]
                air[i] = rand_nums2[idx_rng2+2]

                pasirtotal += pasir[i]
                batutotal += batu[i]
                airtotal += air[i]
                idx_rng2 += 3
            print(
                f"Mengerahkan {banyak_jin_pembangun} jin untuk membangun candi dengan total bahan {pasirtotal} pasir, {batutotal} batu, dan {airtotal} air.")
            # mengecek apakah semua bahan cukup
            cnt = 0
            if arr_bahan_bangunan[1][2] >= pasirtotal:
                cnt += 1
            if arr_bahan_bangunan[2][2] >= batutotal:
                cnt += 1
            if arr_bahan_bangunan[3][2] >= airtotal:
                cnt += 1
            if cnt == 3:  # jika ketiga bahan cukup
                animasicandi()
                print(
                    f"Jin berhasil membangun total {banyak_jin_pembangun} candi.")
                arr_bahan_bangunan[1][2] -= pasirtotal
                arr_bahan_bangunan[2][2] -= batutotal
                arr_bahan_bangunan[3][2] -= airtotal
                # Menghitung banyaknya candi
                i = 0
                while True:
                    if candi[i][0] == None:
                        break
                    else:
                        i += 1
                banyak_candi = i - 1

                # Memasukkan nama jin ke list candi
                for i in range(banyak_jin_pembangun):
                    # Membuat array untuk ditambahkan ke dalam file
                    if banyak_candi < 100:
                        # Menggabungkan list ke dalam file candi
                        idd = f"{banyak_candi+1}"
                        candi[banyak_candi + 1] = [int(idd), list_pembangun[i], pasir[i], batu[i], air[i], None]
                        banyak_candi += 1
                    else:
                        break
            else:  # jika ada bahan kurang
                pasir_kurang = pasirtotal - arr_bahan_bangunan[1][2]
                batu_kurang = batutotal - arr_bahan_bangunan[2][2]
                air_kurang = airtotal - arr_bahan_bangunan[3][2]
                # output bahan yang kurang
                print("Bangun gagal. Kurang ", end="")
                if pasir_kurang < 0 and batu_kurang < 0:
                    print(f"{air_kurang} air.")
                elif pasir_kurang < 0 and air_kurang < 0:
                    print(f"{batu_kurang} batu.")
                elif batu_kurang < 0 and air_kurang < 0:
                    print(f"{pasir_kurang} pasir.")
                elif pasir_kurang < 0:
                    print(f"{batu_kurang} batu, dan {air_kurang} air.")
                elif batu_kurang < 0:
                    print(f"{pasir_kurang} pasir, dan {air_kurang} air.")
                elif air_kurang < 0:
                    print(f"{pasir_kurang} pasir, dan {batu_kurang} batu.")
                else:
                    print(
                        f"{pasir_kurang} pasir, {batu_kurang} batu, dan {air_kurang} air.")
        else:  # jika tidak ada jin pengumpul
            print(
                "Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    else:
        print("Program ini hanya dapat diakses oleh Bondowoso")
    return arr_bahan_bangunan, idx_rng2, candi