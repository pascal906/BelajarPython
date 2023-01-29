# Operasi Aritmatika

a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a, '+', b, '=', hasil)

# operasi pengurangan -
hasil = a - b
print(a, '-', b, '=', hasil)

# operasi perkalian *
hasil = a * b
print(a, 'x', b, '=', hasil)

# operasi pembagian /
hasil = a / b
print(a, ':', b, '=', hasil)
# print(type(hasil)) pada python, pembagian jika hasilnya desimal akan otomatis jadi float

# operasi eksponen (pangkat) **
hasil = a ** b
print(a, '^', b, '=', hasil)

# operasi modulus (sisa bagi) %
hasil = a % b
print(a, '%', b, '=', hasil)

# operasi floor division //
hasil = a // b
print(a, '//', b, '=', hasil) # dibulatkan ke bawah
# ini semua merupakan operator standar dalam matematika

# prioritas operasi, operational precedence
x = 3
y = 2   
z = 4

# hasil = x ** y * z + x / y - y % z // x
hasil = x ** y * (z + x) / y - y % z // x # yang dalam kurung () akan diselesaikan terlebih dahulu
print(x, '**', y, '*', z, '+', x, '/', y, '-', y, '%', z, '//', x,'=', hasil)

# dalam operasi matematika di python, ada prioritas operasi:
# - ()
# - eksponen (pangkat) **
# - perkalian (*), pembagian (/), dkk seperti % //
# - pertambahan (+) dan pengurangan (-)

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)
# kurung akan mengambil langkah paling pertama
hasil = (x + y) * z
print('(',x,'+',y,') *',z,'=',hasil)
