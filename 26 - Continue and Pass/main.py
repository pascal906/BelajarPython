# Control Flow
# Continue, Pass, Break

# Pass, berfungsi sebagai dummy, tidak akan dieksekusi.

# angka = 0

# while angka < 5:
#     angka += 1
#     if angka == 3:
#         pass # ini tidak akan dieksekusi
#     print(angka)

# Continue

angka = 0
print(f'angka sekarang = {angka}')
while angka < 5:
    angka += 1
    print(f'angka sekarang = {angka}') # aksi 1

    if angka == 3:
        print('Nice!')
        continue # akan membuat loop meloncat ke step selanjutnya
    print('whatsssup') # aksi 2, akan di skip jika ada continue

print('Finish!')