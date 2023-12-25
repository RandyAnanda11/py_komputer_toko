'''kalkulator diskon'''

total_belanja = int(input("masukan total harga : "))

if total_belanja>1000000 :
    harga_diskon = total_belanja - (total_belanja*1/10)
    print(total_belanja, " diskon 10% menjadi ", harga_diskon)

elif total_belanja>=500000 and total_belanja<=1000000 :
    harga_diskon = total_belanja - (total_belanja*3/100)
    print(total_belanja, " diskon 3% menjadi ", harga_diskon)

else :
    print(total_belanja)+6