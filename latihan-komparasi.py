
x = float(input("masukan inputan x : "))
y = float(input("masukan inputan Y : "))
"""if x>y :
    print(x," lebih besar dari ", y)
else :
    print (x," lebih kecil dari ", y)"""

z = float(input("masukan angka yang ditentukan : "))

if z<x and z<y :
    print ("tepi kiri")
if z>x and z>y :
    print ("tepi kanan")
if z==x or z==y :
    print("adalah sama")
else :
    print ("diantara")


