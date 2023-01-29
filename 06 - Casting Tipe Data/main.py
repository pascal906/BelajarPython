# Casting Tipe Data
# casting berarti mengubah tipe data ke tipe data yg lain
# misalkan:

## Data INTEGER
data_int = 0
print("data =", data_int,",type =", type(data_int))

# tipe data = int, float, str, bool
# untuk mengubah tipe data, digunakan operator casting
# seperti dibawah:
data_float = float(data_int)
data_string = str(data_int)
data_bool = bool(data_int)
# untuk boolean, jika nilai 0 maka false, dan selain 0 akan true
print("data =", data_float,",type =", type(data_float))
print("data =", data_string,",type =", type(data_string))
print("data =", data_bool,",type =", type(data_bool))

## Data FLOAT
print("====FLOAT====")
data_float = 9.9
print("data =", data_float,",type =", type(data_float))
data_int = int(data_float) # dibulatkan ke bawah
data_string = str(data_float)
data_bool = bool(data_float) # bernilai false, jika float = 0, else bernilai true
print("data =", data_int,",type =", type(data_int))
print("data =", data_string,",type =", type(data_string))
print("data =", data_bool,",type =", type(data_bool))

## Data BOOLEAN
print("====BOOLEAN====")
data_bool = False # true akan bernilai 1 int, 1.0 float, dan false bernilai 0 int, 0.0 flaot
print("data =", data_bool,",type =", type(data_bool))
data_int = int(data_bool) # dibulatkan ke bawah
data_string = str(data_bool) # pada string akan diubah jadi teks false atau true tergantung nilai pada bool
data_float = float(data_bool) # bernilai false, jika float = 0, else bernilai true
print("data =", data_int,",type =", type(data_int))
print("data =", data_string,",type =", type(data_string))
print("data =", data_float,",type =", type(data_float))

## Data STRING
print("====STRING====")
data_string = "Ucup"
print("data =", data_string,",type =", type(data_string))
# data_int = int(data_string) # string harus angka
data_bool = bool(data_string) # false jika string kosong
# data_float = float(data_string) # string harus angka 
# print("data =", data_int,",type =", type(data_int))
print("data =", data_bool,",type =", type(data_bool))
# print("data =", data_float,",type =", type(data_float))

# Casting berbeda-beda perlakukannya sesuai dengan tipe data