# Copy List
# Teknik menduplikat list

a = ['Ucup', 'Otong', 'Dudung']
print(f'a = {a}')

b = a # pass by reference
print(f'b = {b}')

# kita akan mengubah member dari a

a[1] = 'Michael' # ternyata mengubah juga pada a
b.sort() # apa yang kita lakukan ke list yg satu akan berdampak ke kedua list
print(f'a = {a}')
print(f'b = {b}')

# address dari kedua list
print(f'address a = {hex(id(a))}')
print(f'address b = {hex(id(b))}')
# ternyata address dari kedua list sama, hal ini lah yang menjadi penyebab hal diatas

# bagaimana cara menduplikat?
print('membuat list c dengan a.copy()')
c = a.copy() # full duplicat
print(f'address a = {hex(id(a))}')
print(f'address b = {hex(id(b))}')
print(f'address c = {hex(id(c))}')

# mencoba
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')

print('ubah data c')
c[0] = 'Mario'
print(f'c = {c}')

print('ubah data a')
a[1] = 'Mario'
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')