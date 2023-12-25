# Input
angka_1 = int(input("Masukkan angka-1: "))
angka_2 = int(input("Masukkan angka-2: "))
angka_3 = int(input("Masukkan angka-3: "))


if angka_1 <= angka_2 <= angka_3:
    angka_kecil = angka_1
    angka_tengah = angka_2
    angka_besar = angka_3
elif angka_1 <= angka_3 <= angka_2:
    angka_kecil = angka_1
    angka_tengah = angka_3
    angka_besar = angka_2
elif angka_2 <= angka_1 <= angka_3:
    angka_kecil = angka_2
    angka_tengah = angka_1
    angka_besar = angka_3
elif angka_2 <= angka_3 <= angka_1:
    angka_kecil = angka_2
    angka_tengah = angka_3
    angka_besar = angka_1
elif angka_3 <= angka_1 <= angka_2:
    angka_kecil = angka_3
    angka_tengah = angka_1
    angka_besar = angka_2
else:  # angka_3 <= angka_2 <= angka_1
    angka_kecil = angka_3
    angka_tengah = angka_2
    angka_besar = angka_1


print("Urutan dari kecil ke besar:", angka_kecil, angka_tengah, angka_besar)
