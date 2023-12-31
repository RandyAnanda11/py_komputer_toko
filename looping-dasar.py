#belajar looping
'''dalam py ada beberapa bentuk loop, tapi umum nya diawali dengan for dan in'''

#loop dengan list

angka_list = [1,2,3,4]
for i in angka_list :
    print (i)
print("\n")


#loop dengan range
for i in range(1,5) :
    print (i)
print("\n")
for i in range(5) :
    print (i)
print("\n")

#loop dengan string
string = "ini contoh"

for huruf in string :
    print (huruf)
print("\n")

#latihan uts loop
for i in range (0,6) :
    for j in range(i) :
        if i%2 != 0 : 
            print ("*", end="")
        else :
            print ("#", end="")
    print(" ")
print("\n")

for i in range (1,6) :
    for j in range(6-i) :
        print ("#", end="")
    print("\n")
print("\n")

for i in range (1,6) :
    for j in range (6-i) :
        print(" ", end="")
    for k in range (i) :
        if i%2 != 0 : print ("*",end=" ")
        else : print("#", end =" ")
    print("\n")
print("\n")

for i in range (1,6) :
    for j in range (i-1) :
        print (" ", end="")
    for k in range(6-i) :
        print ("*", end=" ")
    print("\n")
print("\n")




