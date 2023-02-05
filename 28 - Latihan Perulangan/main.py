# Latihan Perulangan

# Membuat segitiga

# # 1.Menggunakan for
# sisi = 5
# # # # dummy variable
# count = 1
# for i in range(sisi):
#     print('*'*count)
#     count += 1
# print('akhir dari for')

# # # 2.Menggunakan while
# count = 1
# while True:
#     print("*"*count)
#     count += 1

#     if count > sisi:
#         break
# print('akhir dari while')

# # 3. Hanya ganjil saja
# count = 1
# while True:
#     # akan print jika ganjil 
#     if (count%2):
#         print("*"*count)
#         count += 1
    
#     # akan kembali ke atas jika ganjil
#     else:
#         count += 1
#         continue
#     # akan break jika count melebihi sisi
#     if count > sisi:
#         break
# print('akhir dari while')

# segitiga sama sisi
sisi = 20
count = 1
spasi = sisi//2
while True:
    if count%2:
        print(' '*spasi, '*'*count)
        count += 1
        spasi -= 1
    else:
        count += 1
        continue

    if count > sisi:
        break
print('akhir dari program')

# Tugas membuat ketupat
