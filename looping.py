#sistem print angka genap
for i in range (1,6) :
    for j in range (i) :
        if i%2 == 0 :
            print ("*", end="")
        else : print("#", end="")
    print ("\n")

'''
i =1 j=1 -> # (ganjil)

i =2 j=1 -> * (genap)
     j=2 -> *
     
i =3 j=1 -> 3
     j=2 -> 3
     j=3 -> 3

i =4 j=1 -> 4
     j=2 -> 4
     j=3 -> 4
     j=4 -> 4

i =5 j=1 -> * (ganjil)
     j=2 -> 5
     j=3 -> 5
     j=4 -> 5
     j=5 -> 5

    
i = kebawah nya (baris)
j = kesampingnya (kolom)

'''