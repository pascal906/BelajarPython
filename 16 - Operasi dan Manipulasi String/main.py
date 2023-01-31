# Operasi dan Manipulasi String

# 1. menyambung string (cancatenate)

nama_pertama = 'Ucup'
nama_tengah = 'D'
nama_akhir = 'Fame'

nama_lengkap = nama_pertama + ' ' + nama_tengah + "'" + nama_akhir
print(nama_lengkap)
# cara di atas adalah concate

# 2. menghitung panjang dari string
panjang = len(nama_lengkap) 
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. operator untuk string
# mengecek apakah ada komponen char atau string di string
d = "Ucup"
status = d in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + ' = ' + str(status))
# kebalikannya
d = "d"
status = d not in nama_lengkap
print("string " + d + " tidak ada di " + nama_lengkap + ' = ' + str(status))

# mengulang string
print('wk'*10)
print(10*'wk') # peletakannya bisa di depan atau belakang

# indexing
print('index ke-0: ' + nama_lengkap[0])
print('index ke-1: ' + nama_lengkap[1])
print('index ke-(-1): ' + nama_lengkap[-1])
print('index ke-(-2): ' + nama_lengkap[-2])
# index minus, akan memanggil index mulai dari belakang

print('index ke-[0:3]: ' + nama_lengkap[0:3])
# pada python, range 0:3 python hanya akan mengambil index 0, 1, 2, sementara 3 tidak diambil.
# jadi range dalam python tidak akan  mengambil index terakhir.
# jika ingin mengambil index 3:7:
print('index ke-[3:8]: ' + nama_lengkap[3:8])
# menggunakan jeda:
print('index ke-[0,2,4,6,8,10]: ' + nama_lengkap[0:11:2])

print('\nitem paling kecil')
min_ascii = min(nama_lengkap)
code_ascii = ord(min_ascii)
print('Kode ASCII dari karakter paling minimal: ', code_ascii)
print('paling kecil: ' + min(nama_lengkap)) # maksudnya nilai ascii_code

print('\nitem paling besar')
max_ascii = max(nama_lengkap)
code_ascii = ord(max_ascii)
print('Kode ASCII dari karakter paling maximal: ', code_ascii)
print('paling besar: ' + max(nama_lengkap))

print('\nuntuk melihat kode ASCII')
# untuk melihat kode ascii dari string
ascii_code = ord("'")
print('ASCII code untuk spasi adalah ' + str(ascii_code))

# jika ingin melihat karakter dari kode ascii:
data = 117
print('char untuk ASCII 117 adalah ' + chr(data))

# 4. operator dalam bentuk method
# string mempunyai method
print('menghitung character tertentu dalam string dengan method')
data = 'otong surotong pararotong'
jumlah = data.count('o')
print('jumlah o pada ' + data + ' = ' + str(jumlah))
