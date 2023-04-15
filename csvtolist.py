def csv_parsing(nama_file, row, collumns): # Fungsi parsing CSV statis
    CSV_List = [[None for j in range(collumns)] for i in range(row)] # CSV yang sudah diparsing akan dimasukkan ke variabel CSV_List
    i = 0
    j = 0
    value = ""
    with open(nama_file, 'r') as file:
        for row in file:
            for char in row:  # loop setiap karakter pada baris
                if char == ";" or char == '\n':  # jika ditemukan titik koma, maka simpan nilai dalam array f
                    CSV_List[i][j] = value
                    value = ""
                    j += 1
                    if j >= 3:  # reset kolom jika sudah mencapai batas kolom maksimal
                        j = 0
                        i += 1
                else:  # tambahkan karakter ke nilai yang sedang dibaca
                    value += char
    return CSV_List
