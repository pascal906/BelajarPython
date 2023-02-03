# Latihan Date and Time

import datetime as dt

# hari_ini = dt.date.today()
# print(hari_ini)
# print(f'Hari ini adalah hari = {hari_ini:%A}')

# tanggal = dt.date(2005, 5, 5)
# print(tanggal)
# print(f'Tanggal lahir adalah = {tanggal:%A}')

print('Silakan masukan tanggal, bulan, dan tahun lahir anda:')
tanggal = int(input('Tanggal \t:'))
bulan = int(input('Bulan \t\t:'))
tahun = int(input('Tahun \t\t:'))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f'Tanggal lahir anda adalah: {tanggal_lahir}')
print(f'Harinya adalah: {tanggal_lahir:%A}')

hari_ini = dt.date.today()
print(f'Hari ini tanggal: {hari_ini}')
umur_hari = hari_ini - tanggal_lahir 
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
# print(umur_tahun)
print(f'Umur anda sekarang adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan')

# membuat aplikasi untuk menghitung umur, bulan, dan hari
