from typing import List, Union

#menghitung panjang list in list
def panjang_arraybesar(array: List[Union[str, int]] | List[str]) -> int:
            i = 0
            while True:
                if array[i][0] == None:
                    break
                else:
                    i += 1
            return i

#menghitung panjang list
def panjang_arraykecil(array: List[Union[str, int]] | List[str]) -> int:
            i = 0
            while True:
                if array[i] == None:
                    break
                else:
                    i += 1
            return i

def list_to_csv(my_list: List[Union[str, int]] | List[str], path: str, filename: str):
    # Membuat string CSV dari list
    csv_string = ''
    for k in range(panjang_arraybesar(my_list)):
        line = ''
        for j in range(panjang_arraykecil(my_list[k])):
            line += str(my_list[k][j]) + ';'
        for i in range(len(line)-1):
            csv_string += line[i]
        if k == panjang_arraybesar(my_list) -1  :
            break
        else:
            csv_string += '\n'

    # Menyimpan string ke dalam file CSV
    with open(f'{path}/{filename}', 'w') as file:
        file.write(csv_string)
