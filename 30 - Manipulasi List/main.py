# Manipulasi List

# Operasi
# index  0/(-3)  1/(-2)   2/(-1)
data = ['Ucup', 'Otong', 'Dudung']

# Mengambil data dari list di atas:
tampil = data[0]
print(f'Data pertama (index 0) = {tampil}')

# mengambil data paling terakhir
tampil = data[-1] # dengan cara memanggil index -1
print(f'Data terakhir adalah = {tampil}')

data_ucup = data[-3]
print(f'data ucup = {data_ucup}')

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f'Panjang data = {panjang_data}')

# # Manipulasi data list
# menambahkan item pada list sesuai posisi
print(f'Data sebelum ditambah = \n{data}')

# data.insert(posisi, item)
data.insert(1, 'Asep')
print(f'Data sesudah ditambah = \n{data}')

# menambah di akhir list
data.append('Jajang')
print(f'Data setelah ditambah = \n{data}')

# menambahkan list dengan list
data_baru = ['Ujang', 'Usep', 'Dadang']
print(f'Ini adalah data baru = \n{data_baru}')

data.extend(data_baru)
print(f'data gabungan = \n{data}')

# merubah data
# kita ubah data 2 otong, menjadi michael
# kita hanya perlu tahu index dari data yang ingin diubah
data[2] = 'Michael'
print(f'Data setelah diubah = \n{data_baru}')

# menghapus data
data.remove('Ujang')
# saat menghapus menggunakan ini data yg ingin dihapus harus sesuai dengan yg kita tuliskan persis sama
print(f'Data setelah dihapus = \n{data}')

# menghapus data paling belakang
data_akhir = data.pop()
print(f'data akhir = \n{data}')

print(f'data yang dihapus = {data_akhir}')