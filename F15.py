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
''')
   elif username == 'Roro':
      print('''=========== HELP ===========
1. logout
   Untuk keluar dari akun yang digunakan sekarang
2. hancurkancandi
   Untuk menghancurkan candi yang tersedia
''')
   #kalau bukan Bondowoso atau Roro, maka adalah Jin
   else:
      for baris in f:
         if baris[0] == username:
            if (baris[2]) == 'Pengumpul': # cek di array f, untuk username tertentu ini rolenya apa
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
