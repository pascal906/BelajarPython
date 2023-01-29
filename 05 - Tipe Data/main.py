# Tipe Data pada Python
# merupakan macam-macam bentuk data yang dapat digunakan dalam python

# sebelumnya kita sudah mengetahui bahwa:
# a = 10, dimana a adalah variabel, dan 10 adalah value/nilai dari variabel

# selanjutnya tipe data apa saja pada python

# tipe data: angka satuan (integer):
data_integer = 1
# ini adalah integer
# untuk mengecek bisa menggunakan:
print("data:", data_integer)
print("bertipe:", type(data_integer))

# tipe data: angka dengan koma (float/desimal)
data_float = 1.5
print("data:", data_float)
print("bertipe:", type(data_float))

# tipe data: kumpulan karakter (string)
data_string = "ucup1"
print("data:", data_string)
print("bertipe:", type(data_string))

# tipe data: biner true/false (0,1) (boolean)
data_bool = True
print("data:", data_bool)
print("bertipe:", type(data_bool))

## tipe data khusus
# bilangan kompleks, dituliskan dalam complex(bilangan real, bilangan imajiner)
data_complex = complex(5,6)
print("data:", data_complex)
print("bertipe:", type(data_complex))

# tipe data bahasa C
# bisa dilakukan jika butuh dengan mengimport tipe data dari c:
from ctypes import c_double, c_char, c_long
# sesuai dgn kebutuhan tinggal pakai (,)
data_c_double = c_double(10.5)
print("data:", data_c_double)
print("bertipe:", type(data_c_double))