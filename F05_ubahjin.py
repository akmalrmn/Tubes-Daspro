from time import sleep

def ubahjin(csvlist, idx_usn):
    if csvlist[idx_usn][0] == "Bondowoso":
        username_jin = input('Masukkan username jin : ')
        for i in range (3, 1001):    
                #logic: jika username di matriks f ada yang punya peran pembangun atau pengumpul maka dia pasti jin
                #logic: selain pembangun atau pengumpul maka bukan jin
                if csvlist[i][0] == username_jin:
                    if csvlist[i][2] == 'Pengumpul':
                        sleep(0.5)
                        print()
                        jawab = input('Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ')
                        if jawab == 'Y':
                            csvlist[i][2] = 'Pembangun'
                            sleep(0.5)
                            print('Jin telah berhasil diubah.')
                            break
                        else:
                            sleep(0.5)
                            print('Jin tidak jadi diubah')
                            break
                    elif csvlist[i][2] == 'Pembangun':
                        sleep(0.5)
                        print()
                        jawab = input('Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ')
                        if jawab == 'Y':
                            csvlist[i][2] = 'Pengumpul'
                            sleep(0.5)
                            print('Jin telah berhasil diubah.')
                            break
                        else:
                            sleep(0.5)
                            print('Jin tidak jadi diubah')
                            break
                #kalau sampai akhir iterasi tidak ditemukan username_jin pada kolom 1 (alias kolom username) pada csvlist, maka
                elif (i+1) == 1001:
                    sleep(0.5)
                    print(f'Tidak ada jin dengan username {username_jin}.')
                    break
    else:
        sleep(0.5)
        print("Program ini hanya dapat diakses oleh Bondowoso")
    return csvlist
