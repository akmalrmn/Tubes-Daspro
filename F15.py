def Help():
   if login == False : # mengacu pada kode di F01 yakni kalau sudah berhasil login maka login = True, kalau belum berhasil login artinya login = False
      print('''=========== HELP ===========
1. login
   Untuk masuk menggunakan akun
2. exit
   Untuk keluar dari program dan kembali ke terminal
''')
   elif username == 'Bondowoso':
      print('''=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. summonjin
   Untuk memanggil jin
3. hapusjin
   Untuk menghapus jin dan candi yang dibuat jin tersebut
4. ubahjin
   Untuk mengubah tipe jin
5. batchkumpul
   Untuk mengerahkan seluruh pasukan jin untuk mengumpulkan bahan atau pembangun
6. laporanjin
   Untuk mengambil laporan jin untuk mengetahui kinerja dari para jin
7. laporancandi
   Untuk mengambil laporan candi untuk mengetahui progress pembangunan candi
''')
   elif username == 'Roro':
      print('''=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. hancurkancandi
   Untuk menghancurkan candi yang tersedia
3. ayamberkokok
   Untuk menyelesaikan permainan dengan memalsukan pagi hari
''')
   #kalau bukan Bondowoso atau Roro, artinya username tsb adalah Jin
   else:
      for baris in f: # dilakukan scanning kesesuaian input username dengan data username di array f
         if baris[0] == username: # memeriksa mulai dari baris pertama dan kolom ke nol (kolom username)
            if (baris[2]) == 'Pengumpul': # cek di array f, untuk username ini rolenya apa, kalau 'Pengumpul' maka print
               print('''=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. kumpul
   Untuk mengumpulkan resource candi
''')
            elif (baris[2]) == 'Pembangun': # cek di array f, untuk username tertentu ini rolenya apa
               print('''=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. bangun
   Untuk membangun candi
''')


# misal
# f = [['Bondowoso', 'cintaroro', 'bandung_bondowoso'],['jin1', 'password', 'Pengumpul' ],['jin2', 'password', 'Pembangun']]
# login = True
# username = 'Roro'
# Help()
