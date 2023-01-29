# Latihan Komparasi dan Logika

# membuat gabungan area rentang dari sebuah angka
# ++++3----10++++

inputUser = float(input('Masukkan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10\n: '))

# ++++3----
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print(inputUser, 'Kurang dari 3', '=', isKurangDari)

# ----10++++
# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print(inputUser, 'Lebih dari 10', '=', isLebihDari)

# menggabungkan dua syarat, hasilnya:
isCorrect = isKurangDari or isLebihDari
print('Angka yang anda masukan:', isCorrect)

print('\n', 10*"=", '\n')
# ----3++++10----
# kasus irisan
inputUser = float(input('Masukkan angka yang bernilai\nlebih dari 3\natau\nkurang dari 10\n: '))

# ----3++++
# memeriksa angka lebih dari 3
isLebihDari = inputUser > 3
print(inputUser, 'Lebih dari 3', '=', isLebihDari)

# ++++10----
# memeriksa angka kurang dari 10
isKurangDari = inputUser < 10
print(inputUser, 'Kurang dari 10', '=', isKurangDari)

# menggabungkan dua syarat, hasilnya:
isCorrect = isKurangDari and isLebihDari
print('Angka yang anda masukan:', isCorrect)