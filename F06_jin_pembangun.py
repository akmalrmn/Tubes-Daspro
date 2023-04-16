def jin_pembangun():
    import random
    import csvtolist
    import listtocsv

    # Convert array dari csv
    arr_candi = csvtolist.csv_to_list('candi.csv',101,5)
    arr_user = csvtolist.csv_to_list('user.csv',1001,3)
    arr_bahan_bangunan = csvtolist.csv_to_list('bahan_bangunan.csv',4,3)
    # print(arr_user)
    
    # Id dari candi yang dibangun
    id = 1
    for i in range (101):
        if arr_candi[i][0] == None and i != 1:
            id = int(arr_candi[i-1][0]) + 1
            break

    # Menghitung banyak candi
    banyak_candi = -1
    for element in arr_candi :
        if element[0] != None :
            banyak_candi += 1
        else :
            break

    # Bahan bangunan yang dibutuhka
    pasir_dibutuhkan = random.randint(1,5)
    batu_dibutuhkan = random.randint(1,5)
    air_dibutuhkan = random.randint(1,5)

    # Sisa bahan bangunan yang sudah dipakai
    sisa_pasir = int(arr_bahan_bangunan[1][2]) - pasir_dibutuhkan
    sisa_batu = int(arr_bahan_bangunan[2][2]) - batu_dibutuhkan
    sisa_air = int(arr_bahan_bangunan[3][2]) - air_dibutuhkan

    # Menghitung banyak jin pembangun dalam array user
    banyak_jin_pembangun = 0
    for user in arr_user :
        if user[2] == "jin_pembangun" :
            banyak_jin_pembangun += 1

    # List nama jin pembangun candi
    nama_jin = [None for i in range (banyak_jin_pembangun)]
    idx = 0
    for user in arr_user :
        if user[2] == "jin_pembangun" :
            nama_jin[idx] = user[0]
            idx += 1
    
    # Mengambil nama jin random dari list nama_jin
    pembuat = random.choice(nama_jin)    

    # Sisa candi yang perlu dibangun
    sisa_bangun_candi = 99 - banyak_candi

    # Algoritma
    if sisa_pasir < 0 or sisa_batu < 0 or sisa_air < 0 :
        print('Bahan bangunan tidak mencukupi.\nCandi tidak bisa dibangun!')
    else :
        if banyak_candi == 100 :
            print('Candi berhasil dibangun.\nSisa candi yang perlu dibangun: 0.')
            arr_bahan_bangunan[1][2] = sisa_pasir
            arr_bahan_bangunan[2][2] = sisa_batu
            arr_bahan_bangunan[3][2] = sisa_air
        else :
            print(f'Candi berhasil dibangun.\nSisa candi yang perlu dibangun: {sisa_bangun_candi}.')
            arr_bahan_bangunan[1][2] = sisa_pasir
            arr_bahan_bangunan[2][2] = sisa_batu
            arr_bahan_bangunan[3][2] = sisa_air
    


    # Membuat array untuk ditambahkan ke dalam file
    if banyak_candi < 100 :
        # Menggabungkan list ke dalam file candi
        arr_candi_baru = [id,pembuat,pasir_dibutuhkan,batu_dibutuhkan,air_dibutuhkan]
        with open('candi.csv', 'a') as file:
            row = ''
            for item in arr_candi_baru:
                row += str(item) + ';'
            file.write(row[:-1] + '\n')

    # Menggabungkan list bahan bangunan ke dalam file bahan bangunan
    listtocsv.list_to_csv(arr_bahan_bangunan, 'bahan_bangunan.csv')
