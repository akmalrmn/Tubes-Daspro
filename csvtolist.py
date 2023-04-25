def csv_to_list(csv_path, row, collumns): # mengubah csv ke list in list
    j = 0
    csv_list = [[None for k in range(collumns)] for i in range(row)]
    with open(csv_path, 'r') as csv: # melakukan read pada file csv
        lines = csv.readlines() # setiap baris pada file csv menjadi sebuah list
        for baris in lines: # membaca setiap baris pada fie csv
            kata_grup = [] # grup kata pada tiap baris
            kata = '' # kata pada tiap kolom
            for i in range (len(baris)): # membaca setiap huruf pada baris
                if baris[i] == ';': # ketika menemukan ;, maka kata pada kolom tersebut sudah selesai
                    if kata.isdigit(): # apabila kata merupakan sepenuhnya angka
                        kata = int(kata)
                    kata_grup += [kata] # dimasukan ke grup kata pd baris
                    kata = '' # isi kata di-reset
                elif baris[i] == '\n': # ketika menemukan baris baru, berarti baris tersebut tidak mempunyai kata lagi
                    if kata.isdigit(): # apabila kata merupakan sepenuhnya angka
                        kata = int(kata)
                    kata_grup += [kata] # kata sebelum baris baru dimasukkan ke grup kata
                    csv_list[j] = kata_grup # grup kata dengan baris i dimasukkan ke list utama
                    j += 1
                    break
                else:
                    kata += baris[i] # list kata akan dimasukkan terus menerus dengan huruf
            else:
                if kata.isdigit(): # apabila kata merupakan sepenuhnya angka
                        kata = int(kata)
                kata_grup += [kata] # ketika tidak menemukan baris baru/sudah pada baris terakhir
                csv_list[j] = kata_grup
    return csv_list
