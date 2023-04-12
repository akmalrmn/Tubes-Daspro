# def ubahjin():
#     if username == 'Bondowoso':
#         username_jin = input('Masukkan username jin : ')
#         if username_jin == 'Jin1':
#             jawab = input('Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)?')
#             if jawab == 'Y':
#                 print('Jin telah berhasil diubah.')
#         elif username_jin == 'Jin2':
#             jawab = input('Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)?')
#             if jawab == 'Y':
#                 print('Jin telah berhasil diubah.')
#         else:
#             print('Tidak ada jin dengan username tersebut.')

# username = 'Bondowoso'
# ubahjin()

# penampung_jenis_jin = [['Jin1','Pengumpul'],['Jin2','Pembangun']]

# def ubahjin():
#     global penampung_jenis_jin
#     if username == 'Bondowoso':
#         username_jin = input('Masukkan username jin : ')
#         if username_jin == 'Jin1':
#             jawab = input(f'Jin ini bertipe {penampung_jenis_jin [0][1]}. Yakin ingin mengubah ke tipe {penampung_jenis_jin [1][1]} (Y/N)?')
#             if jawab == 'Y':
#                 penampung_jenis_jin [0][1] = penampung_jenis_jin [1][1]
#                 print('Jin telah berhasil diubah.')
#         elif username_jin == 'Jin2':
#             jawab = input(f'Jin ini bertipe {penampung_jenis_jin [1][1]}. Yakin ingin mengubah ke tipe {penampung_jenis_jin [0][1]} (Y/N)?')
#             if jawab == 'Y':
#                 penampung_jenis_jin [1][1] = penampung_jenis_jin [0][1]
#                 print('Jin telah berhasil diubah.')
#         else:
#             print('Tidak ada jin dengan username tersebut.')

# username = 'Bondowoso'
# ubahjin()
# print(penampung_jenis_jin)

# from jenis_jin import penampung_jenis_jin

# def ubahjin():
#     global penampung_jenis_jin
#     if username == 'Bondowoso':
#         username_jin = input('Masukkan username jin : ')
#         if username_jin == 'Jin1':
#             jawab = input(f'Jin ini bertipe {penampung_jenis_jin[0][1]}. Yakin ingin mengubah ke tipe {penampung_jenis_jin[1][1]} (Y/N)?')
#             if jawab == 'Y':
#                 penampung_jenis_jin[0][1] = penampung_jenis_jin[1][1]
#                 save_jenis_jin()
#                 print('Jin telah berhasil diubah.')
#         elif username_jin == 'Jin2':
#             jawab = input(f'Jin ini bertipe {penampung_jenis_jin[1][1]}. Yakin ingin mengubah ke tipe {penampung_jenis_jin[0][1]} (Y/N)?')
#             if jawab == 'Y':
#                 penampung_jenis_jin[1][1] = penampung_jenis_jin[0][1]
#                 save_jenis_jin()
#                 print('Jin telah berhasil diubah.')
#         else:
#             print('Tidak ada jin dengan username tersebut.')

# username = 'Bondowoso'
# ubahjin()


def count_rows(arr):
    row_count = 0
    for row in arr:
        row_count += 1
    return row_count


def ubahjin():
    if username == 'Bondowoso':
        username_jin = input('Masukkan username jin : ')
        for i in range (count_rows(f))   # f = jadi_array('user.csv',baris,kolom) yang bikin zaki:
                #logic: jika username di matriks f ada yang punya peran pembangun atau pengumpul maka dia pasti jin
                #logic: selain pembangun atau pengumpul maka bukan jin
                if f[i][0] == username_jin:
                    if f[i][2] == 'Pengumpul':
                        jawab = input('Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)?')
                        if jawab == 'Y':
                            f[i][2] == 'Pembangun'
                            print('Jin telah berhasil diubah.')
                    elif f[i][2] == 'Pembangun':
                        jawab = input('Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)?')
                        if jawab == 'Y':
                            f[i][2] == 'Pengumpul'
                            print('Jin telah berhasil diubah.')
                    else:
                        #kalau masuk ke else, artinya input username memang ada tapi bukan jin, misal username_jin == 'Bondowoso', 
                        #maka if f[i][0] = 'Bondowoso', tetapi role bondowoso bukan pengumpul atau pembangun, sehingga dia bukan jin
                        print('Tidak ada jin dengan username tersebut.')
                #kalau sampai akhir iterasi tidak ditemukan username_jin pada kolom 1 (alias kolom username) pada f, maka
                elif (i+1) == count_rows(f):
                    print('Tidak ada jin dengan username tersebut.')