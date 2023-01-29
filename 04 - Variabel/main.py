# Variabel adalah tempat untuk menyimpan data/nilai

# misalkan:
a = 10
# maka a bernilai 10
x = 5
# x bernilai 5
# ini disebut peletakan nilai atau assignment nilai
# jadi pada python, tidak memiliki deklarasi seperti:
# int = a, namun pada python akan langsung assignment nilai ke variabelnya:
# seperti x = 5
# namun menamai variabel tidak hanya dengan satu huruf saja,
# bisa lebih dari satu atau dalam bentuk kata
panjang = 1000

'''untuk memanggil variabel atau nilai variabel
bisa menggunakan dengan cara print'''
# pemanggilan pertama variabel
print(a)

# Jika ingin menyisipkan text, bisa dengan cara berikut:
print("nilai dari a adalah",a)

'''selama variabelnya sudah di assignment seperti di atas
kita dapat memanggilnya di bawah'''

print("Nilai dari x adalah", x)
print("Nilai panjang adalah", panjang)

# aturan pembuatan variabel

# nama y = yosua x
# nama-y = yosua x
# pada nama variabel tidak boleh ada spasi, atau -,
# jika ingin menggunakan spasi pakai _ (underscore)
# nama_y = yosua v

# 10juta = 10000000 x
# pada awal nama variabel tidak bisa menggunakan angka
# meletakkan angka pada variabel hanya bisa di gunakan
# jika angkanya diletakkan di belakang nama variabel:
# juta10 = 10000000 v
nilaiZ = 17.5 #ini boleh

# apakah nilai variabel hilang jika telah dipanggil?
# tidak
# variabel dapat dipanggil berkali-kali

# pemanggilan kedua
print("nilai dari a adalah",a)
print("Nilai dari x adalah", x)
print("Nilai panjang adalah", panjang)

# kita juga dapat mengubah assigment nilai yang ada,
# dengan cara, membuat assignment nilai baru ke variabel yg sudah ada
# contoh nilai a sebelumnya adalah 10,
a = 8
print("nilai dari a adalah",a)
# maka nilai a akan berubah jadi 8

# kita juga bisa memberi nilai pada variabel,
# berdasarkan nilai dari variabel lain
# hal ini disebut dengan assignment indirect
# contoh:
b = a
# hal ini membuat variabel baru yakni b memiliki nilai
# yang sama dengan variabel a
print("Nilai b adalah", b)