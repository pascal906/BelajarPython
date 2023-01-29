import time
# Latihan Perhitungan Sederhana

# Konversi Suhu
# Celcius ke satuan lain
start_time = time.time()

print("PROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('Masukkan suhu dalam Celcius: '))
print("Suhu adalah", celcius, "Celcius")

# Reamur (4/5) * celcius
reamur = (4/5) * celcius
print("Suhu adalah", reamur, "Reamur")

# Fahrenheit ((9/5) * celcius) + 32
fahrenheit = ((9/5) * celcius) + 32
print("Suhu adalah", fahrenheit, "Fahrenheit")
# Kelvin celcius + 273
kelvin = celcius + 273
print("Suhu adalah", kelvin, "Kelvin")

print(time.time() - start_time, "detik")