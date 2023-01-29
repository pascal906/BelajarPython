# Operator Assignment
# Operasi yang dapat dilakukan dengan penyingkatan
# Operasi ditambah dengan assignment

# misalkan:
a = 5 # ini adalah assignment
print('nilai a =', a)

# a = a + 1 # operasi ini bisa kita permudah/persingkat
# menjadi
a += 1 # ini artinya a = a + 1
print('nilai a += 1 =', a) # dan hasilnya sama
print('nilai a saat ini:', a)
# hal ini juga bisa dilakukan dengan operator lain
a -= 2 # artinya adalah a = a - 2
print('nilai a -= 2 =', a) # dan hasilnya sama

# perkalian
a *= 5 # artinya adalah a = a * 5
print('nilai a *= 5 =', a)

# pembagian
a /= 2 # artinya adalah a = a / 2
print('nilai a /= 2 =', a) # tipe datanya otomatis berubah jadi float.

# modulus
b = 10
print('\nnilai b =', b)

b %=3
print('nilai b %= 2, nilai b menjadi', b)

# floor division
b = 10
print('\nnilai b =', b)

b //= 3
print('nilai b //= 2, nilai b menjadi', b)

# perpangkatan
a = 5
print('nilai a =', a) 

a **= 3
print('nilai a **= 2, nilai a menjadi', a)

# Operasi assignment bisa digunakan untuk bitwise
# Operasi Bitwise
# OR
c = True
print('\nnilai c =', c)
c |= False
print('nilai c |= False, nilai c menjadi', c)

c = False
print('\nnilai c =', c)
c |= False
print('nilai c |= False, nilai c menjadi', c)

# AND
c = True
print('\nnilai c =', c)
c &= False
print('nilai c &= False, nilai c menjadi', c)

c = True
print('\nnilai c =', c)
c &= True
print('nilai c &= True, nilai c menjadi', c)

# XOR
c = True
print('\nnilai c =', c)
c ^= False
print('nilai c ^= False, nilai c menjadi', c)

c = True
print('\nnilai c =', c)
c ^= True
print('nilai c ^= True, nilai c menjadi', c)

# geser geser
d = 0b0100
print('\nnilai d =', format(d,'04b'))
d >>= 2
print('nilai d >>= 2, nilai d menjadi', format(d,'04b'), 'biner')
print('nilai d >>= 2, nilai d menjadi', d)

d = 0b0100
d <<= 1
print('nilai d <<= 1, nilai d menjadi', format(d,'04b'), 'biner')
print('nilai d <<= 1, nilai d menjadi', d)
