# list -> array, mengakses data dengan index
data_list = ["Ucup", "Otong", "Dudung"]
print(data_list[0])

# DICTIONARY
# dictionary (dict) -> associative array
# menggunakan identifier untuk mengakses data
# identifier -> key

data_dict = {
    'key':'value',
    'cp':'ucup',
    'tg':'otong',
    'dg':'dudung',
    'nmbr': 100,
    'list': data_list
}

print(data_dict['tg'])
# sangat bagus untuk data yang berstruktur
print(data_dict['nmbr'])
print(data_dict['list'])
# bisa untuk integer, ataupun list, jadi bebas mau isi tipe data apa
# bahkan bisa masukkan dictionary dalam dictionary