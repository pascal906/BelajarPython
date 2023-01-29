# Kelvin ke Fahrenheit
# ((9/5) * (kelvin - 273)) + 32
kelvin = float(input("Masukkan input suhu Kelvin: "))
fahrenheit = ((9/5) * (kelvin - 273.15)) + 32
print("Suhu adalah", fahrenheit, "Fahrenheit")

# Fahrenheit ke Kelvin
# ((5/9) * (fahrenheit - 32)) + 273
fahrenheit = float(input("Masukkan input suhu Fahrenheit: "))
kelvin = ((5/9) * (fahrenheit - 32)) + 273.15
print("Suhu adalah", kelvin, "Kelvin")