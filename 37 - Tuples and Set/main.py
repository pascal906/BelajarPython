# TUPLES and SET
# menggunakan kurung siku
data_list = [10, 2, 4, 3, 2]
print(data_list)
print(type(data_list))

# tuples
data_tuples = (7, 8, 9, 10)
print(data_tuples)
print(type(data_tuples))
print(data_tuples[1])

# data tuples tidak bisa diubah
# data_tuples[1] = "Ucup"
# 'tuple' object does not support item assignment  

# data_tuples.append(1)
# 'tuple' object has no attribute 'append'

# gunanya data tuples?
# untuk data yang akan selalu konstan, dan tidak berubah-ubah

# SET
# sebuah koleksi data yang tidak punya indeks
data_sets = {10, 4, 3, 2, 4, 7, 6, 5}
print(data_sets)

# merupakan himpunan yang tidak memiliki indeks
# print(data_sets[0])
# 'set' object is not subscriptable