data = 'Ini adalah string'
print(data)
print(type(data))

# 1. Cara membuat string
# string adalah kumpulan dari beberapa karakter, a-z, A-Z, 0-9, dll

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''
# spasi masih merupakan komponen dari string
data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"') # tanda yang ada "" di dalamnya akan dianggap string
print("'Halo, apa kabar?'") # yg ditampilkan adalah kutip 1

print("ini adalah hari jum'at")
# penggunaan tanda kutip '' atau "" disesuaikan dengan konteks string yang digunakan.

# 2. Menggunakan tanda \ (backslash)
# membuat tanda ' menjadi string
print('mari shalat jum\'at') 
# dengan backslash tadi, ' pada kata jum'at akan dianggap string
print('g\'day, isn\'t it?')
# setiap tanda ' yg memang tidak termasuk string gunakan \ agar mereka dianggap string

# backslash
# print("C:\user\Ucup")
# agar backslash dicetak sebagai string, tambahin satu backslash lagi, jadi \\.
print("C:\\User\\Ucup")

# tab, digunakan \t dan bisa digunakan berkali-kali
print("ucup\totong, jauhan")
print("ucup\t\t\totong, jauhan")
print("ucup\t\t\t\t\totong, jauhan")

# backspace (\b) akan menghilangkan satu spasi ke depan
print("ucup \botong, jadi deketan")

# newline (\n)
print("baris pertama.\nbaris kedua.")
# LF -> line feed
print("baris pertama.\rbaris kedua.")
# CR -> carriage return
print("baris pertama.\r\nbaris kedua.")
# CRLF line feed carriage return

# LF, jika anda pada unix, linux, atau macos -> LF, artinya untuk mendeteksi newline, digunakan lF
# CR, digunakan pada commodore, acorn, lisp
# CRLF, dipakai pada windows
# jadi ini adalah konvensi digunakan untuk mendeteksi enter

# 3. String literal atau raw
# hati-hati
print('C:\new folder') # akan salah pathnya
print('C:\\new folder') # nah akan berhasil,
# yang jadi masalah jika kita memiliki banyak kasus yang sama seperti di atas.

# solusinya, kita menggunakan raw string
print(r'menggunakan raw string')
print(r'C:\new folder')
# semua elemen-elemen backslash tadi akan dianggap raw

print(r'C:\new\b\t\nfolder\\n') # semuanya akan di print karena dianggap string

# multiline literal string
print("""
Nama: Ucup
Kelas: 3 SD
""")

# multiline literal string dan RAW
print(r"""
Nama : Ucup
Kelas : 3 SD\newnormal
Website : www.ucup.com/newID
""")
# semua yang ada dalam """...""" akan dianggap karakter string