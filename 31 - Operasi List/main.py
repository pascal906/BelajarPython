# Operasi List

data_angka = [ 1, 2, 4, 6, 2, 5, 7, 8, 1, 3, 7, 9, 4, 3]
print(f'Data angka = \n{data_angka}')

# count data
# menghitung berapa kali data yang muncul dalam list
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)
print(f'Jumlah data 4 = {jumlah_data_4}')
print(f'Jumlah data 3 = {jumlah_data_3}')

# ambil posisi data (mengambil index)
data = ['Ucup', 'Otong', 'Ujang', 'Dudung']
print(f'data = {data}')
index_dudung = data.index('Dudung')
index_ujang = data.index('Ujang')
print(f'Posisi (index) Dudung = {index_dudung}')
print(f'Posisi (index) Ujang = {index_ujang}')

# mengurutkan list
print(f'data angka sebelum diurutkan = \n{data_angka}')
data_angka.sort() # int diurutkan berdasarkan angka terkecil ke terbesar
print(f'data angka sort = \n{data_angka}')
data.sort() # str diurutkan berdasarkan abjad
print(f'data angka sort = \n{data}')

# balik listnya
data_angka.reverse()
print(f'data yang diurutkan terbalik = \n{data_angka}')
data.reverse()
print(f'data yang diurutkan terbalik = \n{data}')
