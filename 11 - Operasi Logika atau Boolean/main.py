# Operasi Logika atau Boolean

# NOT, OR, AND, XOR

# NOT
print('=== NOT ===')
a = False
c = not a
print('Data boolean =', a)
print('---------- NOT')
print('Data boolean =', c)

# OR (jika salah satu nilainya True, berarti True, dan jika kedua nilainya False, berarti False)
print('=== OR ===')
a = True
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = True
c = a or b
print(a, 'OR', b, '=', c)
a = True
b = True
c = a or b
print(a, 'OR', b, '=', c)

# AND (jika salah satu nilainya false, maka akan false, hanya akan true jika kedua nilainya true)
print('=== AND ===')
a = True
b = False
c = a and b
print(a, 'AND', b, '=', c)
a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)
a = False
b = True
c = a and b
print(a, 'AND', b, '=', c)
a = True
b = True
c = a and b
print(a, 'AND', b, '=', c)

# XOR (true jika salah satu nilainya true, sisanya false)
print('=== AND ===')
a = True
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)
a = True
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)