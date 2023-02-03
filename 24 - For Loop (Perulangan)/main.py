# Perulangan (loop)

#  for kondisi:
#     aksi

angka_list = [0, 2, 4, 8, 10] # ini adalah list
print(angka_list)

for i in angka_list:
    print(f'i sekarang = {i}')
print('akhir dari program 1\n')

# dengan range
angka_range = range(1,6)

for i in angka_range:
    print(f'i sekarang = {i}')
    # print('saya Keren')
print('akhir dari program 2\n')

# menggunakan data string

data_str = "saya ganteng abiees"
for huruf in data_str:
    print(huruf)

print('akhir dari program 3\n ')