# looping dari list

# for loop
print('\nMenggunakan For Loop - Angka')
kumpulan_angka = [4, 3, 2, 5, 6, 1]
# for {var} in {list}
for angka in kumpulan_angka:
    print(f'angka = {angka}')

print('\nMenggunakan For Loop - String')
peserta = ['ucup', 'otong', 'dadang', 'dudung']

for nama in peserta:
    print(f'nama = {nama}')

# for loop dan range
print('\nFor Loop - Range')
kumpulan_angka = [10, 5, 4, 2, 6, 5]
panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f'angka = {kumpulan_angka[i]}')

# menggunakan while
print('\nMenggunakan While')
kumpulan_angka = [10, 5, 4, 2, 6, 5]
panjang = len(kumpulan_angka)

i = 0
while i < panjang:
    print(f'angka = {kumpulan_angka[i]}')
    i += 1

# list comprehension
print('\nList Comprehension')
data = ['ucup', 1, 2, 3, 'otong']

[print(f'data = {i}') for i in data]

# kuadrat angka
print('\nMembuat kuadrat dari list')
angka = [10, 5, 4, 2, 6, 5]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# enumerate
print('\nEnumerate')
data_list = ['ucup', 1, 2, 3, 'otong']

for index, data in enumerate(data_list):
    print(f'index = {index}, data = {data}')