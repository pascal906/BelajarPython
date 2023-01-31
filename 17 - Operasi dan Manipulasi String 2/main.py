# Operasi dan Manipulasi String

# operator method

# # mengubah case dari string

salam = 'bro!'
print('normal =' + salam)
salam = salam.upper()
print('normal =' + salam)

alay = 'aKu KeCe AbiezZzZZZZZ'
print('normal = ' + alay)
alay = alay.lower()
print('normal = ' + alay)

# # pengecekan dengan isX method
# contoh pengecekan lower case
salam = 'sist!'
apa_lower = salam.islower() # hasilnya boolean
print(salam + ' is lower = ' + str(apa_lower))

apa_upper = salam.isupper() # hasilnya boolean
print(salam + ' is upper = ' + str(apa_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab, newline \n
# istitle() <-- semua kata dimulai dengan huruf besar

# isalpha()
alpha = 'hurufsemua' # hanya akan mengecek karakter string huruf semua atau tidak
cekalpha = alpha.isalpha()
print(alpha + ' is alpha = ' + str(cekalpha))

alpha = 'huruf semua' # jika ada spasi atau karakter lain selain huruf akan dianggap false
cekalpha = alpha.isalpha()
print(alpha + ' is alpha = ' + str(cekalpha))

# isalnum()
alnum = 'sebagianhurufdan123' # hanya mengecek angka dan huruf
cekalnum = alnum.isalnum()
print(alnum + ' is alnum = ' + str(cekalnum))

alnum = 'sebagianhurufdan1,2,3' # jika ada karakter lain maka akan false
cekalnum = alnum.isalnum()
print(alnum + ' is alnum = ' + str(cekalnum))

# istitle()
judul = 'It Is Okay Not To Be Orkay'
cek_judul = judul.istitle() # hasil bool
# dalam penulisan judul tidak pakai '' atau "", setiap awal kata huruf besar, jika tidak sesuai maka nilainya false.
print(judul + ' is title = ' + str(cek_judul))

# # mengecek komponen startswith(), endswith() <-- keren
cek_start = 'Sangjangnim Oppa'.startswith('Sangjangnim')
print('start = ' + str(cek_start)) # karakter deteksinya harus sama

cek_end = 'Sangjangnim Oppa'.endswith('Oppak')
print('end = ' + str(cek_end)) # karakter deteksinya harus sama
# saat mengecek, betul-betul harus sama persis

# # penggabungan komponen join(), split()
pisah = ['aku', 'sayang', 'kamu']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabung = ' '.join(pisah)
print(gabung)

gabung = ' ehmm '.join(pisah)
print(gabung)

gabung = 'akuehmsayangehmkamu'
print(gabung.split('ehm')) # akan tersplit dan menjadi list lagi

# # alokasi karakter rjust(), ljust(), center()
print(5*'=' + 'data' + '='*5)

# rjust()
kanan = 'kanan'.rjust(10)
print("'" + kanan + "'")

# ljust()
kiri = 'kiri'.ljust(10)
print("'" + kiri + "'")

# # center(width[, fillchar])
# untuk membuat string tertentu berada tepat di tengah sesuai dengan width yang ditentukan
# dan filchar akan menjadi pengisi space kiri dan kanan
tengah = 'tengah'.center(10)
print("'" + tengah + "'")

# bagaimana jika karakter sampingnya bukan spasi?
tengah = 'tengah'.center(30,"=")
print("'" + tengah + "'")

# kebalikannya -> strip()
tengah = tengah.strip("=") # menghilangkan tanda =
print("'" + tengah + "'")

# masih banyak method lain yang ada, 
# tugasnya cari method-method lain dan apa kegunaannya

# capitalize()
# membuat suatu teks string capitalize di awal kalimat.
string = 'capitalize format membuat string awal kata menjadi capitalize.'.capitalize()
string2 = 'ini string lanjutan untuk di coba.'.capitalize()
print(string + ' ' + string2)


# count(sub[, start[, end]])
# decode
# encode([encoding[, errors]])
# endswith(suffix[, start[, end]])
# expandtabs([tabsize])
# find(sub[, start[, end]])
# format(*args, **kwargs)
# index(sub[, start[, end]])
# isalnum()
# isalpha()
# isdigit()
# islower()
# isspace()
# istitle()
# isupper()
# join(iterable)
# ljust(width[, fillchar])
# lower()
# lstrip([chars])
# partition(sep)
# replace(old, new[, count])
# rfind(sub[, start[, end]])
# rindex(sub[, start[, end]])
# rjust(width[, fillchar])
# rpartition(sep)
# rsplit([sep[, maxsplit]])
# rstrip([chars])
# split([sep[, maxsplit]])
# splitlines([keepends])
# startswith(prefix[, start[, end]])
# strip([chars])
# swapcase
# title()
# translate(table[, deletechars])
# upper()
# zfill(width)
# isnumeric()
# isdecimal()