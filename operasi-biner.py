#ddefinisikan fungsi display

#bit wise digunakan untuk mengubah suatu angka hexadesimal menjadi angka biner 8 bit

a = 8
b = 3

"""print("nilai bitwise dari ", a, "adalah ", format(a,"08b"))"""

#dengan menggunakan gerbang logika kita akan melakukan operasi binari

# and
syntax_and = a & b
#or
syntax_or = a | b
#xor
syntax_xor = a^b
#not
syntax_not = ~syntax_or

print("nilai bitwise dari ", syntax_or, "adalah ", format(syntax_or,"08b"))