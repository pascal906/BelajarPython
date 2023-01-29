# Operator Bitwise, disebut juga operasi biner, binary
# bitwise -> masing-masing bit

# misalkan
#     76543210 - orde, letak akan menjadi pangkat dari 2 = 2^orde
# 2 = 00000010 = 2^1
# 1 = 00000001 = 2^0
# 9 = 00000101 = 2^3 + 2^0 = 8 + 1

# bitwise adalah operasi antara biner
# contoh:
# 2 | 1 -> | dalam bitwise adalah or
# 2 = 00000010 _ 0 = false, 1 = true
# 1 = 00000001 _ menggunakan operasi or, ingat or pada logika
#     00000011 = 2^1 + 2^0 = 3

# operator bitwise
# or, and, xor, not

a = 9
b = 5

# bitwise OR (|)
c = a | b
print('==== OR ====')
print('Nilai:', a, ', Binary:', format(a, '08b'))
print('Nilai:', b, ', Binary:', format(b, '08b'))

print('==== (|) ====')
print('Nilai:', c, ', Binary:', format(c, '08b'))

# bitwise AND (&)
c = a & b
print('\n==== AND ====')
print('Nilai:', a, ', Binary:', format(a, '08b'))
print('Nilai:', b, ', Binary:', format(b, '08b'))

print('==== (&) ====')
print('Nilai:', c, ', Binary:', format(c, '08b'))

# bitwise XOR (^)
c = a ^ b
print('\n==== XOR ====')
print('Nilai:', a, ', Binary:', format(a, '08b'))
print('Nilai:', b, ', Binary:', format(b, '08b'))

print('==== (^) ====')
print('Nilai:', c, ', Binary:', format(c, '08b'))

# bitwise NOT (~)
# a = 0
c = ~a
print('\n==== NOT ====')
print('Nilai:', a, ', Binary:', format(a, '08b'))

print('==== (~) ====')
print('Nilai:', c, ', Binary:', format(c, '08b'))
# mirroring angka positif, akan menghasilkan negatif, yg dimulai dari -1, bagian positif dimulai dari 0
# oleh karena itu saat a = 0, maka ~a = -1

d = 0b0000001001
e = 0b1111111111
print('==== (^) ====')
print('Nilai:', e ^ d, ', Binary:', format(e ^ d, '08b'))

# Shifting
# shift right (>>)
c = a >> 2 # akan menggeser nilai biner ke arah kanan sebanyak yg diinginkan
print('\n==== SHIFTING ====')
print('Nilai:', a, ', Binary:', format(a, '08b'))

print('==== (>>) ====')
print('Nilai:', c, ', Binary:', format(c, '08b'))

# shift left (<<)
c = a << 2 # akan menggeser nilai biner ke arah kiri sebanyak yg diinginkan
print('\n==== SHIFTING ====')
print('Nilai:', a, ', Binary:', format(a, '08b'))

print('==== (<<) ====')
print('Nilai:', c, ', Binary:', format(c, '08b'))

# di python semua angka itu signed