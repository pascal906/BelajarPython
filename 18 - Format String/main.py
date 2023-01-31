# Format String

# contoh generic, f
# string
nama = 'marlene'
str1 = 'hello ' + nama + ', apa kabar?'
print(str1)

format_str = f'hello {nama}'
# konstruksi sebuah string dengan format  
print(format_str)

# angka
# angka = 2005.5
# format_str = 'angka = ' + str(angka)
# print(format_str)

angka = 2005.5
format_str = f'angka = {angka}'
print(format_str)

# boolean
boolstr = False
format_str = f'boolean = {boolstr}'
print(format_str)

# bilangan bulat
angka = 15
format_str = f'bilangan bulat = {angka:d}' # :d untuk menampilkan format integer, jika yg dipanggil bukan integer akan error
print(format_str)

# bilangan ordo ribuan
angka = 2000000
format_str = f'bilangan jutaan = {angka:,}' # memberi koma (,) pada angka
print(format_str)

# bilangan desimal
angka = 2005.53421
format_str = f'desimal = {angka:.3f}' # :.2f membatasi angka dibelakang (,) menjadi 2
print(format_str)

# meanmpilkan leading zero
angka = 2005.53421
format_str = f'desimal = {angka:9.3f}' # : angka 9 pada 9.2f itu menandakan banyak angka didepan koma (,) sebanyak 9 angka
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = -10
format_minus = f'minus = {angka_minus:+d}' # +d untuk menampilkan + atau - pada angka
format_plus = f'plus = {angka_plus:+.2f}' # juga bisa digunakan pada format .2f atau float numbers

print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f'persen = {persentase:.2%}' # .2% untuk menampilkan 2 angka belakang (,) pada format persen

print(format_persen)

# melakukan operasi aritmatika di dalam placeholder
# misalkan:
harga = 10000
jumlah = 5

format_string = f'harga total = Rp. {harga*jumlah:,}'
print(format_string) 

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f'binary = {bin(angka)}'
format_octal = f'octal = {oct(angka)}'
format_hex = f'hex = {hex(angka)}'

print(format_binary)
print(format_octal)
print(format_hex)