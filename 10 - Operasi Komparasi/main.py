# Operasi Komparasi
# untuk membandingkan nilai

# setiap hasil dari operasi komparasi adalah boolean
# operator:
# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# lebih dari (>)
print("lebih dari (>)")
hasil = a > 3
print (a, '>', 3, '=', hasil)
hasil = b > 3
print (b, '>', 3, '=', hasil)
hasil = b > 2
print (b, '>', 2, '=', hasil)

# kurang dari (<)
print("\nkurang dari (<)")
hasil = a < 3
print (a, '<', 3, '=', hasil)
hasil = b < 3
print (b, '<', 3, '=', hasil)
hasil = b < 2
print (b, '<', 2, '=', hasil)

# lebih dari sama dengan (>=)
print("\nlebih dari sama dengan (>=)")
hasil = a >= 3
print (a, '>=', 3, '=', hasil)
hasil = b >= 3
print (b, '>=', 3, '=', hasil)
hasil = b >= 2
print (b, '>=', 2, '=', hasil)

# kurang dari sama dengan (<=)
print("\nkurang dari sama dengan (<=)")
hasil = a <= 3
print (a, '<=', 3, '=', hasil)
hasil = b <= 3
print (b, '<=', 3, '=', hasil)
hasil = b <= 2
print (b, '<=', 2, '=', hasil)

# jika = berjumlah satu, disebut assignment
# jika == berjumlah dua, disebut sama dengan (komparasi)
# sama dengan (==)
print("\nkurang dari sama dengan (==)")
hasil = a == 4
print (a, '==', 4, '=', hasil)
hasil = b == 3
print (b, '==', 3, '=', hasil)
hasil = b == 2
print (b, '==', 2, '=', hasil)

# sama dengan (!=)
print("\nkurang dari sama dengan (!=)")
hasil = a != 4
print (a, '!=', 4, '=', hasil)
hasil = b != 3
print (b, '!=', 3, '=', hasil)
hasil = b != 2
print (b, '!=', 2, '=', hasil)

# saat melakukan komparasi di python,
# semua operasi komparasi di atas tadi dapat kbekerja pada syntax literal
# contoh: a == 4
# a ada nilainya, 4 literal
# a memakan memory, beda dengan 4 tertulis langsung

# nah, operator is, membandingkan pada nilai yang memakan memori (membandingkan memory/objek)
# contoh: a is 4 ini tidak bisa
# berlaku pada:
# a = 4
# b = 4
# a is b, pada komparasi ini is bisa digunakan

# 'is' sebagai komparasi object identity
print('=== Object Identity (is) ===')
x = 5 # ini adalah assignment membuat object
y = 5

# nilai id dari kedua variabel berbeda di atas adalah sama.
# hal ini karena python sudah cerdas untuk mendeteksi nilai yg sama pada variabel,
# dan memasukkan ke id atau alamat memory yang sama. Hal ini membuat pengolahan variabel menjadi lebih efisien
print('nilai x = ',x,',id = ',hex(id(x)))
print('nilai y = ',y,',id = ',hex(id(y)))
hasil = x is y
# hasil = x is 5 jika ingin membandingkan dgn literal lebih baik menggunakan ==
# karena jika tetap menggunakan is, akan menyebabkan warning dari python
print('x is y =', hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x = ',x,',id = ',hex(id(x)))
print('nilai y = ',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =', hasil)
# saat nilai variabel berbeda, maka akan disimpan pada alamat memory yg berbeda
# sehingga hasil komparasi is menjadi False

print('=== Object Identity (is not) ===')
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x = ',x,',id = ',hex(id(x)))
print('nilai y = ',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x = ',x,',id = ',hex(id(x)))
print('nilai y = ',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is not y =', hasil)
