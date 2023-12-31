from ast import Str
import time # mengimport data dari package time
from ctypes import c_double 

x = 2
y = x+1 
z = str(y)
data_cdouble = c_double(0.5)
# print variable dan tipe data 
print("nilai x = ", x, "nilai y = ", y, "tipe data z adalah ", type(z)) 

#menghitung waktu running time
start_time = time.time() #unix time semenjak 1 januari 1970
print(time.time() - start_time) 

# menginput data  dan meng-castingnya kedalam type data integer
data = int(input("masukin data nya"))

# mengompile file pyhton dengan skrip berikut untuk mengubah menjadi bytecode
""" python -m py_compile [nama file nya.py]"""

#kemudian berikan promp berikut untuk mengeksekusi bytecode
"""python __/pycache__/[nama file bytecode.py]"""

# menggunakan  data yang sudah di input 
data = data + 1
print (data)

#operasi komparasi 
""" lebih dari """
if x>y :
    print("x lebih besar dari y")

""" kurang dari """
if x<y : 
    print("x lebih kecil dari y")

""" sama dengan"""
if x==y :
    print ("x adalah sama dengan y")

""" tidak sama dengan"""
if x!=y : 
    print ("x tidak sama dengan y")

if x>=y or x<=y :
    print ("x dia lebih besar atau lebih kecil dari y")
    
#operasi logika dan bolean 
""" operasi bolean dalam py, yaitu """
a=True
b=False

hasil_and = a and b
hasil_or = a or b
hasil_xor = a^b 
hasil_not = not hasil_and; """not and artinya or"""

#operasi binari(bitwise) 

binari_and = x & y 
print(format(binari_and,"08bit"))

binari_or = x|y
print(format(binari_or,"08bit"))

binari_xor = x^y
print(format(binari_xor,"08bit"))

binari_not = not binari_or
print(format(binari_not,"08bit"))
