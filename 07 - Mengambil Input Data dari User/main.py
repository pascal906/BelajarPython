# Mengambil Input Data dari User

data = input("Masukkan data: ")
print("Data =", data, ",type =", type(data))
# data yang dimasukkan akan terbaca sebagai str
# jadi jika kita ingin mengambil integer, maka data masukan kita casting ke integer:
# data_int = int(data)
# print("Hasil casting = ", data_int, ",type =", type(data_int))

# atau:
angka = int(input("Masukkan data: "))
angka = float(input("Masukkan data: "))
print("Data =", angka, ",type =", type(angka))

# bagaimana dengan boolean
# untuk nilai boolean kita perlu untuk casting ke integer sebelum casting ke boolean
# simplenya seperti ini:
biner = bool(int(input("Masukkan nilai boolean: ")))
print("Data =", biner, ",type =", type(biner))