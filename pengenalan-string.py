
'''print ("makan apa hari ini \nmakan ikan hari ini")
print ("saya akan tab kalimat dibawah disamping \tokelah gw ke tab")
print ("c:\\new folder")'''

#belajar operasi pada string
'''Concatenation : hanya bisa pada kumpulan string'''

nama_depan = "randy"
nama_tangah = " aulia"
nama_belakang = " ananda ruslani"

nama_lengkap = nama_depan +nama_tangah +nama_belakang
print(nama_lengkap)

'''menghitung panjang suatu string'''

contoh_kalimat = "ini adalah saya"
print ("panjang dari "+ contoh_kalimat + " adalah " + str(len(contoh_kalimat)) )

'''mengecek apakah suatu elemen ada di dalam string'''

cek_r = "r" in contoh_kalimat 
print(cek_r)
cek_not_b = "b" not in contoh_kalimat
print(cek_not_b)

'''mengakses salah satu elemen dalam string'''
print(nama_depan[-2]) 
print(nama_depan[0:5])

''' menghitung banyak element'''
data = "assalamualaikum"
banyak_element = data.count("s")
print(banyak_element)

'''indeks paling kecil paling besar'''
print(max(data))
print(min(data))

'''mengubah case dari lower to upper atau sebaliknya'''

besarin = "anjing"
kecilin = "ASTAGAAA"

print(besarin.upper())
print(kecilin.lower())

# contoh program yang mengecek upper dan lower
contoh = str(input ("masukan contoh kalimat "))
if contoh.islower() :
    print(contoh + " adalah lowercase")

else : 
    print("kalimat " + contoh + " telah dilower menjadi " + contoh.lower() )


 