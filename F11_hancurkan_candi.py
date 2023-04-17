def hancurkan_candi():
    import csvtolist
    import listtocsv

    # Mengubah file candi.csv menjadi list
    list_candi = csvtolist.csv_to_list('candi.csv',101,5)

    # Input id candi 
    id_candi = input('Masukan ID candi: ')

    # Cek apakah ada candi dengan ID tersebut dan declare atas nama valid
    valid = False
    for candi in list_candi:
        if candi[0] == id_candi:
            valid = True
    
    # Algoritma Hancurkan_candi
    if not valid :
        print('Tidak ada candi dengan ID tersebut.')        
    else :
        pilihan = input('Apakah anda yakin ingin menghancurkan candi ID: 5 (Y/N)? ')
        if pilihan == 'N' :
            print("Candi gagal dihancurkan.")
        elif pilihan == 'Y' :
            # cari baris candi dengan ID tersebut
            loop = True
            row_num = 0
            i = 0
            while loop:
                if list_candi[i][0] != id_candi:
                    i += 1
                    row_num += 1
                else :
                    loop = False

    # Menghapus elemen pada list dengan ID candi tersebut
    list_candi = list_candi[:row_num] + list_candi[(row_num+1):]

    # Mengubah list menjadi file candi.csv
    listtocsv.list_to_csv(list_candi,'candi.csv')
    
    return
