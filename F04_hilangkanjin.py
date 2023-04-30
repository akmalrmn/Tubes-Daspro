from time import sleep
from typing import List, Tuple, Union

def hapus_jin(user: List[str], candi: List[Union[str, int]], idx_usn: int) -> Tuple[List[str], List[Union[str, int]]]:
    # fungsi buat hitung len array
    def panjang_array(array: List) -> int:
        i = 0
        while True:
            if array[i][0] == None:
                break
            else:
                i += 1
        return i

    # fungsi hapus jin
    def hapus_jin(nama_jin: str, array_user: List[str]) -> List[str]:
        for i in range (panjang_array(array_user)):
            if nama_jin == array_user[i][0]:
                array_user[i][0] = ""
        return array_user

    # fungsi hapus candi
    def hapus_candi_jin(nama_jin: str, array_candi: List[Union[str, int]]) -> List[Union[str, int]]:
        for i in range (panjang_array(array_candi)):
            if nama_jin == array_candi[i][1]:
                array_candi[i][1] = ""
        return array_candi

    # habis dihapus, data yang dikanannya geser ke kiri
    # contoh [1,"",3,None] --> [1,3,None]
    def geser_arr_user(array_user: List[str]) -> List[str]:
        arr = [[None for _ in range(4)] for _ in range (1003)]
        j = 0
        for i in range (panjang_array(array_user)):
            if array_user[i][0] != "":
                arr[j] = array_user[i]
                j += 1
        return arr

    # habis dihapus, data yang dikanannya geser ke kiri
    # contoh [1,"",3,None] --> [1,3,None]
    def geser_arr_candi(array_candi: List[Union[str, int]]) -> List[Union[str, int]]:
        arr = [[None for _ in range(6)] for _ in range (102)]
        j = 0
        for i in range (panjang_array(array_candi)):
            if array_candi[i][1] != "":
                arr[j] = array_candi[i]
                j += 1
        return arr
    
    # fungsi buat bikin array baru
    def array_bersih_user(array: List[str]) -> List[str]:
        arr = [[None for j in range(4)] for i in range (1001)]
        for i in range (panjang_array(array)):
            arr[i] = array[i]
        return arr
    
    def array_bersih_candi(array: List[Union[str, int]]) -> List[Union[str, int]]:
        arr = [[None for j in range(6)] for i in range (102)]
        for i in range (panjang_array(array)):
            arr[i] = array[i]
        return arr

    if user[idx_usn][0] == "Bondowoso":
        jin = input("Masukkan username jin: ")
        for i in range (panjang_array(user)):
            if jin == user[i][0]:
                sleep(0.5)
                confirm = input(f"Apakah anda yakin ingin menghapus jin dengan username {jin} (Y/N)? ")
                if confirm == "Y":
                    user = array_bersih_user(geser_arr_user(hapus_jin(jin, user)))
                    candi = array_bersih_candi(geser_arr_candi(hapus_candi_jin(jin, candi)))
                    sleep(0.5)
                    print()
                    print(f"{jin} telah berhasil dihapus dari alam gaib.")
                    break
                else:
                    sleep(0.5)
                    print(f"{jin} tidak jadi dihapus.")
                    break
        else:
            sleep(0.5)
            print(f"Tidak ada jin dengan username {jin}.")
    else:
        print("Program ini hanya dapat diakses oleh Bondowoso")
    return user, candi