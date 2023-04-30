from typing import List, Union

def csv_to_list(csv_path: str, row: int, collumns: int) -> List[Union[str, int]]:  # mengubah csv ke list in list
    i = 0
    j = 0

    csv_list = [[None for k in range(collumns)] for i in range(row)]
    with open(csv_path, 'r') as csv:  # melakukan read pada file csv
        kata = ''
        while True:
            huruf = csv.read(1) # membaca huruf satu per satu
            if huruf == ";":
                if kata.isdigit(): # mengecek apabila string hanya mengandung angka saja
                    kata = int(kata) # string dijadikan integer
                csv_list[i][j] = kata # dimasukan ke csv list
                kata = ''
                j += 1
            elif huruf == "\n": # apabila membuat baris baru/ baris sudah habis
                if kata.isdigit():
                    kata = int(kata)
                csv_list[i][j] = kata
                kata = ''
                j = 0
                i += 1
            elif huruf == "": # apabila sudah tidak ada lagi sesuatu di csv
                if kata.isdigit():
                    kata = int(kata)
                csv_list[i][j] = kata
                break
            else:
                kata += huruf # huruf dimasukkan ke kata
    return csv_list
