
print ("kalkulatol cedelhana if else".center(40,'='))
#masukan inputan operasi 
operator = input("masukan input yang anda inginkan\ntambah(+)\nkali(*)\nbagi(/)\nkurang\nmodulo(%)\n.....")
angka1 = float(input("masukan angka ke-1 "))
angka2 = float(input("masukan angka ke-2 "))

if operator == "tambah" :
    print("hasilnya adalah ",angka1+angka2)
elif operator == "kurang" :
    print("hasilnya adalah ",angka1-angka2)
elif operator == "bagi" :
    print ("hasilnya adalah ",angka1/angka2)
elif operator == "kali" :
    print ("hasilnya adalah ",angka1*angka2)
elif operator == "modulo" :
    print ("hasilnya adalah ",angka1%angka2)
else :
    print("operator tidak dikenali")

