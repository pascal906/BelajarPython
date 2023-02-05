# List
# Kumpulan data

data_angka = [1, 5, 2, 3]
print(data_angka)

# Kumpulan data string

data_str = ['Ucup', 'Otong', 'Mario']
print(data_str)

# Kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# Kumpulan campuran data
data_campuran = [1, 'bala-bala', 2, 'cireng', 'ucup', True, 'otong', False]
print(data_campuran)

# cara alternatif membuat list
data_range = range(0, 10, 2) # range(start, stop, step)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop,
# list comprehension

list_pake_for = [i**10 for i in range(0, 10)] # bisa di kuadratkan listnya menggunakan variable i
print(list_pake_for)

# membuat list dengan for dan if
list_pake_for_if = [i for i in range(0, 10) if i != 5]
print(list_pake_for_if)

list_pake_for_if = [i**2 for i in range(0, 10) if i % 2 != 0]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0, 10) if i % 2 == 0]
print(list_pake_for_if)
