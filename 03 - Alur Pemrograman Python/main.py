import time
start_time = time.time()
print("Hello")
print("World")
print("Hello World")

print("Helllo guys")
# ini adalah comment
'''ini adalah comment
multiline'''
a = 10
print(a)
for i in range(1,1000):
    a = 10
'''kita bisa mengcompile code python
ke dalam bentuk bytecode'''
print(time.time() - start_time, "detik")
# cara mengcompile file python dengan mengetikkan:
# python -m py_compile namafile
# pada terminal