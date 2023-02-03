# Kalkulator Sederhana

# angka1 = float(input('Masukkan angka pertama: '))
# operator = input('Masukkan operator (+, -, *, /): ')
# angka2 = float(input('Masukkan angka kedua: '))

# if operator == '+':
#     hasil = angka1 + angka2
#     print(f'Hasilnya adalah {angka1} + {angka2} = {hasil}')
# elif operator == '-':
#     hasil = angka1 - angka2
#     print(f'Hasilnya adalah {angka1} - {angka2} = {hasil}')
# elif operator == '*':
#     hasil = angka1 * angka2
#     print(f'Hasilnya adalah {angka1} * {angka2} = {hasil}')
# elif operator == '/':
#     hasil = angka1 / angka2
#     print(f'Hasilnya adalah {angka1} / {angka2} = {hasil}')
# else:
#     print('operator yang anda masukkan tidak dikenali')

print(20*'=')
print('Kalkulator Sederhana')
print(20*'=' + '\n')

angka_1 = float(input('Masukkan angka 1 = '))
operator = input('operator (+, -, *, /): ')
angka_2 = float(input('Masukkan angka 2 = '))

if operator == '+':
    hasil = angka_1 + angka_2
    print(f'hasilnya adalah {hasil}')
elif operator == '-':
    hasil = angka_1 - angka_2
    print(f'hasilnya adalah {hasil}')
elif operator == '*' or operator == 'x':
    hasil = angka_1 * angka_2
    print(f'hasilnya adalah {hasil}')
elif operator == '/':
    hasil = angka_1 / angka_2
    print(f'hasilnya adalah {hasil}')
else:
    print('masukan yang bener dong!, aku pusing')
print('Akhir dari Program')