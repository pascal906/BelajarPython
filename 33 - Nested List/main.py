# Nested List

data_0 = [1, 2]
data_1 = [3, 4, 5]

data_list_biasa = [1, 2, 3, 4]

print(f'List biasa = {data_list_biasa}')
list_2d = [data_0, data_1, data_list_biasa, 2, 4]

print(f'List 2D = {list_2d}')

# gunanya buat apa?
# ini untuk data yang berseri
# contoh penggunaan:

peserta_0 = ['Ucup', 25, 'Laki-laki']
peserta_1 = ['Otong', 10, 'Laki-laki']
peserta_2 = ['Dedeh', 50, 'Perempuan']

list_peserta = [peserta_0, peserta_1, peserta_2]

print(f'Peserta = {list_peserta}')

for peserta in list_peserta:
    print(f'Nama:\t {peserta[0]}')
    print(f'Umur:\t {peserta[1]}')
    print(f'Gender:\t {peserta[2]}\n')
# inilah salah satu penggunaan nested list
# namun ada beberapa permasalah 
# beberapa operasi kita tidak bisa lakukan pada nested list
# dengan reference

list_copy = list_peserta.copy()
print(f'Peserta = {list_copy}')

peserta_0[0] = 'Michael'
print(f'Peserta = {list_copy}')
print(f'Peserta = {list_peserta}')
