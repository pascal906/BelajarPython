# Mengatur flow dari program (control flow)
# IF and ELSE Statement

# 1. if nya
# 2. kondisinya
# 3. aksinya

nama = input('siapa nama anda? ')
# program sebelumnya
# if kondisi: aksi
# program selanjutnya

# 1. program if inline   
# if nama == 'ucup' : print('Kamu ganteng abis')
# print(f'terima kasih {nama}')

# dalam python ada yang disebut indentation
# 2. program if indentation
print(5*'=' + 'with indentation' + 5*'=')
if nama == 'ucup':
    print('kamu ganteng abis')
    print('kamu juga keren banget')
    # bagian ini masih masuk bagian if
    # untuk keluar dari if tinggal hapus indentasinya
print(f'Terima kasih {nama}')

# 3. else statement
print(5*'=' + 'else statement' + 5*'=')
if nama == 'otong':
    print('hai otongg, si keren!!')
else:
    print('ah kamu bukan otong, kamu gak keren!')
print('akhir dari program')