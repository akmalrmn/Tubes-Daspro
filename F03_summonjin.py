def count_rows(arr):
    row_count = 0
    for row in arr:
        row_count += 1
    return row_count

def count_kata_jin(CSV_List):
    count_kata_jin = 0
    for baris in CSV_List:
        if baris[2] is not None and (baris[2] == "Pengumpul" or baris[2] == 'Pembangun'):
            count_kata_jin += 1
    return count_kata_jin

from time import sleep
from animasi import animasijin

def summonjin(CSV_List, i):
    if count_kata_jin(CSV_List) > 101:
        print('Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu')
        return None
    elif CSV_List[i][0] == "Bondowoso":
        print('''Jenis jin yang dapat dipanggil:
        (1) Pengumpul - Bertugas mengumpulkan bahan bangunan
        (2) Pembangun - Bertugas membangun candi
        ''')
    
        bool_nomor_jin = True
        while bool_nomor_jin:
            sleep(0.5)
            nomor_jin = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
            sleep(0.5)
            if nomor_jin not in ['1', '2']:
                print(f"Tidak ada jenis jin bernomor \“{nomor_jin}\”!")
                print()
            elif nomor_jin == '1':
                print()
                bool_nomor_jin = False
                print('Memilih jin “Pengumpul”.')
                bool_username_jin = True
                while bool_username_jin:
                    sleep(0.5)
                    username_jin = input('Masukkan username jin: ')
                    if username_jin in [row[0] for row in CSV_List]: #buat cara mengetahui apakah username_jin sudah ada di matriks
                        print(f'Username {username_jin} sudah diambil!')
                    else: #jika username_jin belum ada maka buat password
                        # buat loop sampai password memiliki len 5-25
                        bool_username_jin = False
                        bool_password = True
                        while bool_password:
                            password_jin = input('Masukkan password jin: ')
                            print()
                            if count_rows(password_jin) > 4 and count_rows(password_jin) < 26:
                                sleep(0.5)
                                print(f'''Mengumpulkan sesajen...
                                Menyerahkan sesajen...
                                Membacakan mantra...
                                Jin {username_jin} berhasil dipanggil!''')
                                new_data = [username_jin,password_jin,'Pengumpul']
                                indeks = None
                                # Mengecek indeks baris paling kecil yang memiliki None untuk kemudian diganti dengan input summonjin yakni [username_jin,password_jin,'Pengumpul']
                                for i, row in enumerate(CSV_List):
                                    if row == [None, None, None]:
                                        indeks = i
                                        break
                                # Mengganti baris pada indeks yang ditemukan dengan data baru
                                if indeks is not None:
                                    CSV_List[indeks] = new_data
                                print()
                                animasijin()
                                bool_password = False
                            else: #jika panjang password tidak 5 sampai 25 karakter
                                print('Password panjangnya harus 5-25 karakter!')
            else: # untuk nomor jin == 2
                bool_nomor_jin = False
                print()
                print('Memilih jin “Pembangun”.')
                bool_username_jin = True
                while bool_username_jin:
                    username_jin = input('Masukkan username jin: ')
                    if username_jin in [row[0] for row in CSV_List]: #buat cara mengetahui apakah username_jin sudah ada di matriks
                        print(f'Username {username_jin} sudah diambil!')
                    else: #jika username_jin belum ada maka buat password
                        # buat loop sampai password memiliki len 5-25
                        bool_username_jin = False
                        bool_password = True
                        while bool_password:
                            password_jin = input('Masukkan password jin: ')
                            print()
                            if count_rows(password_jin) > 4 and count_rows(password_jin) < 26:
                                sleep(0.5)
                                print(f'''Mengumpulkan sesajen...
                                Menyerahkan sesajen...
                                Membacakan mantra...
                                Jin {username_jin} berhasil dipanggil!''')
                                new_data = [username_jin,password_jin,'Pengumpul']
                                indeks = None
                                # Mengecek indeks baris paling kecil yang memiliki None untuk kemudian diganti dengan input summonjin yakni [username_jin,password_jin,'Pengumpul']
                                for i, row in enumerate(CSV_List):
                                    if row == [None, None, None]:
                                        indeks = i
                                        break
                                # Mengganti baris pada indeks yang ditemukan dengan data baru
                                if indeks is not None:
                                    CSV_List[indeks] = new_data
                                print()
                                animasijin()
                                bool_password = False
                            else: #jika panjang password tidak 5 sampai 25 karakter
                                print('Password panjangnya harus 5-25 karakter!')
    else:
        print("Program ini hanya dapat diakses oleh Bondowoso")
    return CSV_List


#contoh aplikasi secara lokal
# CSV_List = [['username','password','role'],['Bondowoso','cintaroro','bandung_bondowoso'],['Roro','gasukabondo','roro_jonggrang'],[None, None, None],[None, None, None],[None, None, None]]
# summonjin(CSV_List, 1)
# print(CSV_List)

