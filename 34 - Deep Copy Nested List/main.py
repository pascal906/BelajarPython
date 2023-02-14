# Deep Copy Nested List

data_0 = [1, 2]
data_1 = [3, 4]

data_2D = [data_0, data_1, 10]
data_2D_copy = data_2D.copy()

print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")

# mengambil data untuk nested list

data = data_2D[1][0]
# untuk posisi pengambilan data penulisannya mirip index matriks,
# data_2D[1][0] berarti akan mengambil nilai dari matriks data_2D dari baris 1 kolom 0
print(f"data = {data}")

# address semuanya
print(f'address asli = {hex(id(data_2D))}')
print(f'address copy = {hex(id(data_2D_copy))}')

print('address dari member ke-1')
print(f'address asli = {hex(id(data_2D[0]))}')
print(f'address copy = {hex(id(data_2D_copy[0]))}')
# ternyata address member dari data asli dan copy sama

data_2D[1][0] = 5
data_2D[2] = 9
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
# copy() shallow copy
# copy()) akan mengcopy address

# solusi dari ini adalah deep.copy()

# deepcopy
from copy import deepcopy

data_2D = [data_0, data_1, 10]
data_2D_deepcopy = deepcopy(data_2D)

print(f'address asli = {hex(id(data_2D))}')
print(f'address copy = {hex(id(data_2D_copy))}')

print('address dari member ke-1')
print(f'address asli = {hex(id(data_2D[0]))}')
print(f'address copy = {hex(id(data_2D_deepcopy[0]))}')

data_2D[1][0] = 30
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
print(f"data deepcopy = {data_2D_deepcopy}")
