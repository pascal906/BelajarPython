# tugas
print('==== Tugas 1 ====')
# 0>x<5 8>x<11
# ----0++++5----8++++11----

# masukan angka
inputUser = float(input('Masukkan angka: '))

# ----0++++
nol = (inputUser > 0)
print(inputUser, 'Lebih dari 0', '=', nol)

# ++++5----
lima = (inputUser < 5)
print(inputUser, 'Kurang dari 5', '=', lima)

# ----8++++
delapan = (inputUser > 8)
print(inputUser, 'Lebih dari 8', '=', delapan)

# ++++11----
sebelas = (inputUser < 11)
print(inputUser, 'Kurang dari 11', '=', sebelas)

isCorrect = nol and lima or delapan and sebelas
print('0 AND 5 OR 8 AND 11:', isCorrect)

print('==== Tugas 2 ====')
# x<0 5>x<8 11>x
# ++++0----5++++8----11++++
inputUser = float(input('Masukkan angka: '))

# ++++0----
nol = (inputUser < 0)
print(inputUser, 'Kurang dari 0', '=', nol)

# ----5++++
lima = (inputUser > 5)
print(inputUser, 'Lebih dari 5', '=', lima)

# ++++8----
delapan = (inputUser < 8)
print(inputUser, 'Kurang dari 8', '=', delapan)

# ----11++++
sebelas = (inputUser > 11)
print(inputUser, 'Lebih dari 11', '=', sebelas)

isCorrect = nol or lima and delapan or sebelas
print('0 OR 5 AND 8 OR 11:', isCorrect)